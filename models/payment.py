from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .enums import PaymentStatus

class Payment(BaseModel):
    """Payment entity model"""
    id: int = Field(..., description="Unique payment identifier")
    credit_card_id: int = Field(..., description="Credit card used for payment")
    customer_id: int = Field(..., description="Customer ID")
    amount: float = Field(..., description="Payment amount")
    merchant_name: str = Field(..., description="Merchant name")
    category: Optional[str] = Field(None, description="Payment category")
    description: Optional[str] = Field(None, description="Payment description")
    transaction_date: Optional[datetime] = Field(None, description="Transaction timestamp")
    status: PaymentStatus = Field(..., description="Payment status")
    reference_number: Optional[str] = Field(None, description="Transaction reference number")

class PaymentCreate(BaseModel):
    """Payment creation request model"""
    credit_card_id: int = Field(..., description="Credit card used for payment")
    amount: float = Field(..., description="Payment amount", gt=0.01)
    merchant_name: str = Field(..., description="Merchant name")
    category: Optional[str] = Field(None, description="Payment category")
    description: Optional[str] = Field(None, description="Payment description")

class PaymentRefund(BaseModel):
    """Payment refund request model"""
    amount: Optional[float] = Field(None, description="Refund amount (full refund if not specified)")

class PaymentListResponse(BaseModel):
    """Response model for payment list"""
    payments: List[Payment] = Field(..., description="List of payments")
    total: int = Field(..., description="Total number of payments")
    pages: int = Field(..., description="Total pages")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")

class SpendingAnalytics(BaseModel):
    """Model for spending analytics data"""
    period: str = Field(..., description="Analytics period")
    total_amount: float = Field(..., description="Total spending amount")
    transaction_count: int = Field(..., description="Number of transactions")
    category_breakdown: Optional[dict] = Field(None, description="Spending by category")
    merchant_breakdown: Optional[dict] = Field(None, description="Spending by merchant")
