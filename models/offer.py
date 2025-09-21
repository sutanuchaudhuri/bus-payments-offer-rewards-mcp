from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Offer(BaseModel):
    """Offer entity model"""
    id: int = Field(..., description="Unique offer identifier")
    title: str = Field(..., description="Offer title")
    description: Optional[str] = Field(None, description="Offer description")
    category: str = Field(..., description="Offer category")
    merchant_id: Optional[int] = Field(None, description="Associated merchant ID")
    merchant_name: Optional[str] = Field(None, description="Associated merchant name")
    discount_percentage: Optional[float] = Field(None, description="Discount percentage")
    max_discount_amount: Optional[float] = Field(None, description="Maximum discount amount")
    min_transaction_amount: Optional[float] = Field(None, description="Minimum transaction amount")
    reward_points: Optional[int] = Field(None, description="Reward points earned")
    start_date: Optional[datetime] = Field(None, description="Offer start date")
    expiry_date: Optional[datetime] = Field(None, description="Offer expiry date")
    is_active: Optional[bool] = Field(None, description="Whether offer is active")

class OfferCreate(BaseModel):
    """Offer creation request model"""
    title: str = Field(..., description="Offer title")
    description: Optional[str] = Field(None, description="Offer description")
    category: str = Field(..., description="Offer category")
    merchant_id: Optional[int] = Field(None, description="Associated merchant ID")
    discount_percentage: Optional[float] = Field(None, description="Discount percentage", ge=0, le=100)
    max_discount_amount: Optional[float] = Field(None, description="Maximum discount amount", ge=0)
    min_transaction_amount: Optional[float] = Field(None, description="Minimum transaction amount", ge=0)
    reward_points: Optional[int] = Field(None, description="Reward points earned", ge=0)
    start_date: datetime = Field(..., description="Offer start date")
    expiry_date: datetime = Field(..., description="Offer expiry date")
    terms_and_conditions: Optional[str] = Field(None, description="Offer terms and conditions")

class OfferActivationRequest(BaseModel):
    """Offer activation request model"""
    customer_id: int = Field(..., description="Customer ID to activate offer for")
