from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CustomerProfileHistory(BaseModel):
    """Customer profile history entity model"""
    id: int = Field(..., description="Unique history record identifier")
    customer_id: int = Field(..., description="Customer identifier")
    customer_name: Optional[str] = Field(None, description="Customer name")
    merchant_id: Optional[int] = Field(None, description="Merchant identifier")
    merchant_name: Optional[str] = Field(None, description="Merchant name")
    offer_id: Optional[int] = Field(None, description="Offer identifier")
    offer_title: Optional[str] = Field(None, description="Offer title")
    payment_id: Optional[int] = Field(None, description="Payment identifier")
    amount_availed: Optional[float] = Field(None, description="Amount of discount/reward availed")
    transaction_amount: Optional[float] = Field(None, description="Transaction amount")
    savings_percentage: Optional[float] = Field(None, description="Savings percentage")
    statement_descriptor: Optional[str] = Field(None, description="Statement descriptor")
    availed_date: Optional[datetime] = Field(None, description="Date offer was availed")
    offer_category: Optional[str] = Field(None, description="Offer category")
    merchant_category: Optional[str] = Field(None, description="Merchant category")
