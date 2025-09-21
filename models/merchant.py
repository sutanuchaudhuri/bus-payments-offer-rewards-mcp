from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from .enums import MerchantCategory

class Merchant(BaseModel):
    """Merchant entity model"""
    id: int = Field(..., description="Unique merchant identifier")
    merchant_id: str = Field(..., description="Merchant's business identifier")
    name: str = Field(..., description="Merchant's business name")
    description: Optional[str] = Field(None, description="Merchant description")
    category: str = Field(..., description="Merchant category")
    website: Optional[str] = Field(None, description="Merchant's website URL")
    contact_email: Optional[str] = Field(None, description="Merchant's contact email")
    phone: Optional[str] = Field(None, description="Merchant's phone number")
    address: Optional[str] = Field(None, description="Merchant's address")
    is_active: Optional[bool] = Field(None, description="Whether merchant is active")
    created_at: Optional[datetime] = Field(None, description="Merchant registration timestamp")

class MerchantCreate(BaseModel):
    """Merchant creation request model"""
    merchant_id: str = Field(..., description="Merchant's business identifier")
    name: str = Field(..., description="Merchant's business name")
    description: Optional[str] = Field(None, description="Merchant description")
    category: MerchantCategory = Field(..., description="Merchant category")
    website: Optional[str] = Field(None, description="Merchant's website URL")
    contact_email: Optional[str] = Field(None, description="Merchant's contact email")
    phone: Optional[str] = Field(None, description="Merchant's phone number")
    address: Optional[str] = Field(None, description="Merchant's address")
