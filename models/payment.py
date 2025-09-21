from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .enums import PaymentStatus

class Payment(BaseModel):
    """Payment entity model"""
    id: int = Field(..., description="Unique payment identifier")
    credit_card_id: int = Field(..., description="Credit card used for payment")
    amount: float = Field(..., description="Payment amount")
    merchant_name: str = Field(..., description="Merchant name")
    merchant_category: Optional[str] = Field(None, description="Merchant category")
    transaction_date: Optional[datetime] = Field(None, description="Transaction timestamp")
    status: PaymentStatus = Field(..., description="Payment status")
    reference_number: Optional[str] = Field(None, description="Transaction reference number")
    description: Optional[str] = Field(None, description="Payment description")

class PaymentCreate(BaseModel):
    """Payment creation request model"""
    credit_card_id: int = Field(..., description="Credit card used for payment")
    amount: float = Field(..., description="Payment amount", gt=0)
    merchant_name: str = Field(..., description="Merchant name")
    merchant_category: Optional[str] = Field(None, description="Merchant category")
    description: Optional[str] = Field(None, description="Payment description")
