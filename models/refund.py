from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from .enums import RefundStatus, RefundType

class RefundRequest(BaseModel):
    """Submit a refund request for booking cancellation, dispute resolution, or goodwill"""
    refund_type: RefundType = Field(..., description="Type of refund request")
    refund_amount: float = Field(..., gt=0, description="Amount to refund")
    reason: str = Field(..., description="Reason for refund")
    booking_id: Optional[int] = Field(None, description="Related booking ID")
    payment_id: Optional[int] = Field(None, description="Related payment ID")

class PointsRefundRequest(BaseModel):
    """Cancel points redemption and refund points to customer"""
    customer_id: int = Field(..., description="Customer ID")
    points_to_refund: int = Field(..., gt=0, description="Points to refund")
    reason: str = Field(..., description="Reason for points refund")

class RefundApproval(BaseModel):
    """Approve a refund request"""
    approved: bool = Field(..., description="Whether refund is approved")
    admin_notes: Optional[str] = Field(None, description="Admin notes for approval/denial")

class RefundDenial(BaseModel):
    """Deny a refund request"""
    denial_reason: Optional[str] = Field(None, description="Reason for denial")

class Refund(BaseModel):
    """Refund entity model"""
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
    """List of refunds with pagination"""
    refunds: List[Refund] = Field(..., description="List of refunds")
    total: int = Field(..., description="Total number of refunds")
    pages: int = Field(..., description="Total pages")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")
