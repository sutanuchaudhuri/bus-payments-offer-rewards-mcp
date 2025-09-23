from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .enums import PaymentStatus

class Payment(BaseModel):
    """Payment transaction record with merchant details and status."""
    id: Optional[int] = Field(None, description="Internal payment ID")
    credit_card_id: int = Field(..., description="ID of the credit card used")
    customer_id: str = Field(..., description="Alphanumeric customer identifier who made the payment")
    amount: float = Field(..., description="Payment amount")
    merchant_name: str = Field(..., max_length=200, description="Name of the merchant")
    merchant_category: Optional[str] = Field(None, description="Category of the merchant")
    description: Optional[str] = Field(None, description="Payment description")
    transaction_date: Optional[datetime] = Field(None, description="When the transaction occurred")
    status: PaymentStatus = Field(..., description="Current payment status")
    reference_number: str = Field(..., max_length=50, description="Unique transaction reference")
    created_at: Optional[datetime] = Field(None, description="Payment creation timestamp")

class PaymentCreate(BaseModel):
    """Request payload for processing a payment"""
    credit_card_id: int = Field(..., description="ID of the credit card to charge")
    amount: float = Field(..., gt=0.01, description="Payment amount")
    merchant_name: str = Field(..., max_length=200, description="Name of merchant or service provider")
    category: Optional[str] = Field(None, max_length=100, description="Optional transaction category for analytics")
    description: Optional[str] = Field(None, max_length=500, description="Optional transaction description or memo")

class PaymentRefund(BaseModel):
    """Payment refund request model"""
    amount: Optional[float] = Field(None, description="Refund amount (full refund if not specified)")

class PaymentListResponse(BaseModel):
    """Paginated list of payments with transaction details"""
    payments: List[Payment] = Field(..., description="List of payments")
    total: int = Field(..., description="Total number of payments matching criteria")
    pages: int = Field(..., description="Total number of pages available")
    current_page: int = Field(..., description="Current page number")
    per_page: int = Field(..., description="Number of payments per page")

class SpendingAnalytics(BaseModel):
    """Model for spending analytics data"""
    period: str = Field(..., description="Analytics period (day, week, month)")
    total_amount: float = Field(..., description="Total spending amount")
    transaction_count: int = Field(..., description="Number of transactions")
    category_breakdown: Optional[dict] = Field(None, description="Spending by category")
    merchant_breakdown: Optional[dict] = Field(None, description="Spending by merchant")
