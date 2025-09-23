from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .enums import CreditCardProduct

class CreditCard(BaseModel):
    """Credit card associated with a customer account."""
    id: Optional[int] = Field(None, description="Internal card ID")
    customer_id: str = Field(..., description="Alphanumeric customer identifier who owns this card")
    card_number: str = Field(..., description="Masked credit card number (only last 4 digits shown)")
    card_holder_name: str = Field(..., max_length=200, description="Name on the credit card")
    expiry_month: int = Field(..., ge=1, le=12, description="Card expiry month")
    expiry_year: int = Field(..., ge=2024, description="Card expiry year")
    product_type: CreditCardProduct = Field(..., description="Credit card product tier")
    card_type: str = Field(..., description="Card brand/network (VISA, MASTERCARD, etc.)")
    credit_limit: float = Field(..., description="Total credit limit")
    available_credit: Optional[float] = Field(None, description="Available credit remaining")
    is_active: bool = Field(..., description="Whether the card is active")
    created_at: Optional[datetime] = Field(None, description="Card creation timestamp")

class CreditCardCreate(BaseModel):
    """Request payload for adding a credit card to a customer"""
    card_number: str = Field(..., description="Credit card number")
    card_holder_name: str = Field(..., max_length=200, description="Name on the credit card")
    expiry_month: int = Field(..., ge=1, le=12, description="Card expiry month")
    expiry_year: int = Field(..., ge=2024, description="Card expiry year")
    product_type: CreditCardProduct = Field(..., description="Credit card product tier")
    card_type: str = Field(..., description="Card brand/network (VISA, MASTERCARD, etc.)")
    credit_limit: float = Field(..., gt=0, description="Total credit limit")
    is_active: Optional[bool] = Field(True, description="Whether the card is active")

class CreditCardUpdate(BaseModel):
    """Request payload for updating a credit card"""
    card_holder_name: Optional[str] = Field(None, max_length=200, description="Name on the credit card")
    expiry_month: Optional[int] = Field(None, ge=1, le=12, description="Card expiry month")
    expiry_year: Optional[int] = Field(None, ge=2024, description="Card expiry year")
    product_type: Optional[CreditCardProduct] = Field(None, description="Credit card product tier")
    card_type: Optional[str] = Field(None, description="Card brand/network (VISA, MASTERCARD, etc.)")
    credit_limit: Optional[float] = Field(None, gt=0, description="Total credit limit")
    available_credit: Optional[float] = Field(None, description="Available credit remaining")
    is_active: Optional[bool] = Field(None, description="Whether the card is active")

class CreditCardListResponse(BaseModel):
    """Response model for list of customer credit cards"""
    credit_cards: List[CreditCard] = Field(..., description="List of credit cards")
    total: int = Field(..., description="Total number of cards")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")
