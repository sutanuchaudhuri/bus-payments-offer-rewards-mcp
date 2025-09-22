from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from .enums import RefundStatus, RefundType

class RefundRequest(BaseModel):
    """Model for refund request submission"""
    refund_type: RefundType = Field(..., description="Type of refund request")
    refund_amount: float = Field(..., description="Amount to refund", gt=0)
    reason: str = Field(..., description="Reason for refund")
    booking_id: Optional[int] = Field(None, description="Related booking ID")
    payment_id: Optional[int] = Field(None, description="Related payment ID")

class PointsRefundRequest(BaseModel):
    """Model for points redemption cancellation request"""
    customer_id: int = Field(..., description="Customer ID")
    points_to_refund: int = Field(..., description="Points to refund", gt=0)
    reason: str = Field(..., description="Reason for points refund")

class RefundApproval(BaseModel):
    """Model for refund approval"""
    approved: bool = Field(..., description="Whether refund is approved")
    admin_notes: Optional[str] = Field(None, description="Admin notes for approval/denial")

class RefundDenial(BaseModel):
    """Model for refund denial"""
    denial_reason: Optional[str] = Field(None, description="Reason for denial")

class Refund(BaseModel):
    """Model for refund entity"""
    id: int = Field(..., description="Refund ID")
    customer_id: Optional[int] = Field(None, description="Customer ID")
    refund_type: RefundType = Field(..., description="Type of refund")
    refund_amount: float = Field(..., description="Refund amount")
    reason: str = Field(..., description="Refund reason")
    status: RefundStatus = Field(..., description="Refund status")
    booking_id: Optional[int] = Field(None, description="Related booking ID")
    payment_id: Optional[int] = Field(None, description="Related payment ID")
    requested_at: datetime = Field(..., description="Request timestamp")
    processed_at: Optional[datetime] = Field(None, description="Processing timestamp")
    admin_notes: Optional[str] = Field(None, description="Admin notes")
    denial_reason: Optional[str] = Field(None, description="Denial reason if denied")

class RefundListResponse(BaseModel):
    """Response model for refund list"""
    refunds: list[Refund] = Field(..., description="List of refunds")
    total: int = Field(..., description="Total number of refunds")
    pages: int = Field(..., description="Total pages")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")
