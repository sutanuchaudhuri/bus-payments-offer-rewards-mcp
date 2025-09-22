from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .enums import CreditCardProduct

class CreditCard(BaseModel):
    """Credit card entity model"""
    id: int = Field(..., description="Unique credit card identifier")
    customer_id: int = Field(..., description="Associated customer ID")
    card_number: str = Field(..., description="Masked credit card number")
    card_holder_name: str = Field(..., description="Name on the card")
    expiry_month: int = Field(..., description="Card expiry month")
    expiry_year: int = Field(..., description="Card expiry year")
    product_type: CreditCardProduct = Field(..., description="Card product type")
    credit_limit: float = Field(..., description="Credit limit amount")
    available_credit: Optional[float] = Field(None, description="Available credit amount")
    is_active: bool = Field(..., description="Whether card is active")
    created_at: Optional[datetime] = Field(None, description="Card creation timestamp")

class CreditCardCreate(BaseModel):
    """Credit card creation request model"""
    card_number: str = Field(..., description="Credit card number")
    card_holder_name: str = Field(..., description="Name on the card")
    expiry_month: int = Field(..., description="Card expiry month", ge=1, le=12)
    expiry_year: int = Field(..., description="Card expiry year")
    product_type: CreditCardProduct = Field(..., description="Card product type")
    credit_limit: float = Field(..., description="Credit limit amount", gt=0)
    is_active: Optional[bool] = Field(True, description="Whether card is active")

class CreditCardUpdate(BaseModel):
    """Credit card update request model"""
    card_holder_name: Optional[str] = Field(None, description="Name on the card")
    expiry_month: Optional[int] = Field(None, description="Card expiry month", ge=1, le=12)
    expiry_year: Optional[int] = Field(None, description="Card expiry year")
    product_type: Optional[CreditCardProduct] = Field(None, description="Card product type")
    credit_limit: Optional[float] = Field(None, description="Credit limit amount")
    available_credit: Optional[float] = Field(None, description="Available credit amount")
    is_active: Optional[bool] = Field(None, description="Whether card is active")

class CreditCardListResponse(BaseModel):
    """Response model for credit card list"""
    credit_cards: List[CreditCard] = Field(..., description="List of credit cards")
    total: int = Field(..., description="Total number of cards")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")
