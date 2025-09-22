from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .enums import MerchantCategory

class Merchant(BaseModel):
    """Merchant entity model"""
    id: int = Field(..., description="Unique merchant identifier")
    merchant_id: str = Field(..., description="Merchant's business identifier")
    name: str = Field(..., description="Merchant's business name")
    description: Optional[str] = Field(None, description="Merchant description")
    category: MerchantCategory = Field(..., description="Merchant category")
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
    is_active: Optional[bool] = Field(True, description="Whether merchant is active")

class MerchantUpdate(BaseModel):
    """Merchant update request model"""
    merchant_id: Optional[str] = Field(None, description="Merchant's business identifier")
    name: Optional[str] = Field(None, description="Merchant's business name")
    description: Optional[str] = Field(None, description="Merchant description")
    category: Optional[MerchantCategory] = Field(None, description="Merchant category")
    website: Optional[str] = Field(None, description="Merchant's website URL")
    contact_email: Optional[str] = Field(None, description="Merchant's contact email")
    phone: Optional[str] = Field(None, description="Merchant's phone number")
    address: Optional[str] = Field(None, description="Merchant's address")
    is_active: Optional[bool] = Field(None, description="Whether merchant is active")

class MerchantListResponse(BaseModel):
    """Response model for merchant list"""
    merchants: List[Merchant] = Field(..., description="List of merchants")
    total: int = Field(..., description="Total number of merchants")
    pages: int = Field(..., description="Total pages")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")

class MerchantCategoryInfo(BaseModel):
    """Model for merchant category information"""
    value: MerchantCategory = Field(..., description="Category value")
    name: str = Field(..., description="Category name")
    description: str = Field(..., description="Category description")

class MerchantCategoriesResponse(BaseModel):
    """Response model for merchant categories"""
    categories: List[MerchantCategoryInfo] = Field(..., description="List of merchant categories")

class MerchantAnalytics(BaseModel):
    """Model for merchant analytics data"""
    total_transactions: int = Field(..., description="Total number of transactions")
    total_amount: float = Field(..., description="Total transaction amount")
    offer_usage: int = Field(..., description="Number of offer usages")
    period_start: datetime = Field(..., description="Analytics period start")
    period_end: datetime = Field(..., description="Analytics period end")
