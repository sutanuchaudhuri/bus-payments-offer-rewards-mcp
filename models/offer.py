from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .enums import OfferCategory

class OfferStatistics(BaseModel):
    """Model for offer statistics"""
    total_activations: int = Field(..., description="Total number of customer activations")
    active_activations: int = Field(..., description="Number of currently active activations")

class Offer(BaseModel):
    """Offer entity model"""
    id: int = Field(..., description="Unique offer identifier")
    title: str = Field(..., description="Offer title")
    description: Optional[str] = Field(None, description="Offer description")
    category: OfferCategory = Field(..., description="Offer category")
    merchant_id: Optional[int] = Field(None, description="Associated merchant ID")
    merchant_name: Optional[str] = Field(None, description="Associated merchant name")
    merchant_category: Optional[str] = Field(None, description="Merchant category")
    discount_percentage: Optional[float] = Field(None, description="Discount percentage")
    max_discount_amount: Optional[float] = Field(None, description="Maximum discount amount")
    min_transaction_amount: Optional[float] = Field(None, description="Minimum transaction amount")
    reward_points: Optional[int] = Field(None, description="Reward points earned")
    max_usage_per_customer: Optional[int] = Field(None, description="Maximum usage per customer")
    start_date: Optional[datetime] = Field(None, description="Offer start date")
    expiry_date: Optional[datetime] = Field(None, description="Offer expiry date")
    is_active: Optional[bool] = Field(None, description="Whether offer is active")
    terms_and_conditions: Optional[str] = Field(None, description="Terms and conditions")
    created_at: Optional[datetime] = Field(None, description="Creation timestamp")

    # Customer-specific fields (only present when customer_id is provided)
    customer_activated: Optional[bool] = Field(None, description="Whether customer has activated this offer")
    activation_date: Optional[datetime] = Field(None, description="Customer activation date")
    used_count: Optional[int] = Field(None, description="Number of times customer used this offer")

    # Statistics (for detailed view)
    statistics: Optional[OfferStatistics] = Field(None, description="Offer statistics")

class OfferCreate(BaseModel):
    """Offer creation request model"""
    title: str = Field(..., description="Offer title")
    description: Optional[str] = Field(None, description="Offer description")
    category: OfferCategory = Field(..., description="Offer category")
    merchant_id: Optional[int] = Field(None, description="Associated merchant ID")
    merchant_name: Optional[str] = Field(None, description="Merchant name (deprecated, use merchant_id)")
    discount_percentage: Optional[float] = Field(None, description="Discount percentage", ge=0, le=100)
    max_discount_amount: Optional[float] = Field(None, description="Maximum discount amount", ge=0)
    min_transaction_amount: Optional[float] = Field(None, description="Minimum transaction amount", ge=0)
    reward_points: Optional[int] = Field(0, description="Reward points earned", ge=0)
    max_usage_per_customer: Optional[int] = Field(1, description="Maximum usage per customer")
    start_date: datetime = Field(..., description="Offer start date")
    expiry_date: datetime = Field(..., description="Offer expiry date")
    terms_and_conditions: Optional[str] = Field(None, description="Offer terms and conditions")
    is_active: Optional[bool] = Field(True, description="Whether offer is active")

class OfferUpdate(BaseModel):
    """Offer update request model"""
    title: Optional[str] = Field(None, description="Offer title")
    description: Optional[str] = Field(None, description="Offer description")
    category: Optional[OfferCategory] = Field(None, description="Offer category")
    merchant_id: Optional[int] = Field(None, description="Associated merchant ID")
    merchant_name: Optional[str] = Field(None, description="Merchant name")
    discount_percentage: Optional[float] = Field(None, description="Discount percentage", ge=0, le=100)
    max_discount_amount: Optional[float] = Field(None, description="Maximum discount amount", ge=0)
    min_transaction_amount: Optional[float] = Field(None, description="Minimum transaction amount", ge=0)
    reward_points: Optional[int] = Field(None, description="Reward points earned", ge=0)
    max_usage_per_customer: Optional[int] = Field(None, description="Maximum usage per customer")
    start_date: Optional[datetime] = Field(None, description="Offer start date")
    expiry_date: Optional[datetime] = Field(None, description="Offer expiry date")
    terms_and_conditions: Optional[str] = Field(None, description="Offer terms and conditions")
    is_active: Optional[bool] = Field(None, description="Whether offer is active")

class OfferActivationRequest(BaseModel):
    """Offer activation request model"""
    customer_id: int = Field(..., description="Customer ID to activate offer for")

class OfferActivation(BaseModel):
    """Offer activation response model"""
    id: int = Field(..., description="Activation ID")
    offer_id: int = Field(..., description="Offer ID")
    customer_id: int = Field(..., description="Customer ID")
    activation_date: datetime = Field(..., description="Activation date")
    is_active: bool = Field(..., description="Whether activation is active")
    usage_count: int = Field(..., description="Number of times used")
    total_savings: float = Field(..., description="Total savings from this offer")

class OfferListResponse(BaseModel):
    """Response model for offer list"""
    offers: List[Offer] = Field(..., description="List of offers")
    total: int = Field(..., description="Total number of offers")
    pages: int = Field(..., description="Total pages")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")

class OfferCategoryInfo(BaseModel):
    """Model for offer category information"""
    value: OfferCategory = Field(..., description="Category value")
    name: str = Field(..., description="Category name")
    description: str = Field(..., description="Category description")

class OfferCategoriesResponse(BaseModel):
    """Response model for offer categories"""
    categories: List[OfferCategoryInfo] = Field(..., description="List of offer categories")
