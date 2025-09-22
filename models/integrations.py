from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field
from .enums import TokenType

class CardTokenRequest(BaseModel):
    """Model for creating a card token"""
    card_id: int = Field(..., description="Credit card ID")
    token_type: TokenType = Field(TokenType.SINGLE_USE, description="Type of token")
    expires_in_hours: int = Field(24, description="Token expiry in hours", ge=1, le=8760)

class CardToken(BaseModel):
    """Model for card token entity"""
    id: str = Field(..., description="Token ID")
    card_id: int = Field(..., description="Associated credit card ID")
    customer_id: int = Field(..., description="Customer ID")
    token_type: TokenType = Field(..., description="Token type")
    is_active: bool = Field(..., description="Whether token is active")
    created_at: datetime = Field(..., description="Creation timestamp")
    expires_at: datetime = Field(..., description="Expiry timestamp")
    last_used_at: Optional[datetime] = Field(None, description="Last usage timestamp")
    usage_count: int = Field(0, description="Number of times used")

class TokenValidationResponse(BaseModel):
    """Response model for token validation"""
    is_valid: bool = Field(..., description="Whether token is valid")
    token: Optional[CardToken] = Field(None, description="Token details if valid")
    error: Optional[str] = Field(None, description="Error message if invalid")

class ShoppingProductSearch(BaseModel):
    """Model for shopping product search"""
    query: Optional[str] = Field(None, description="Search query")
    category: Optional[str] = Field(None, description="Product category")
    brand: Optional[str] = Field(None, description="Product brand")
    min_price: Optional[float] = Field(None, description="Minimum price", ge=0)
    max_price: Optional[float] = Field(None, description="Maximum price", ge=0)
    page: int = Field(1, description="Page number", ge=1)
    per_page: int = Field(20, description="Items per page", ge=1, le=100)

class ShoppingCartItem(BaseModel):
    """Model for adding item to cart"""
    customer_id: int = Field(..., description="Customer ID")
    product_id: str = Field(..., description="Product ID")
    quantity: int = Field(1, description="Quantity", ge=1)

class ShoppingOrder(BaseModel):
    """Model for creating shopping order"""
    customer_id: int = Field(..., description="Customer ID")
    shipping_address: dict = Field(..., description="Shipping address details")
    payment_method: str = Field(..., description="Payment method (credit_card or points)")

class IntegrationStatus(BaseModel):
    """Model for integration status"""
    service: str = Field(..., description="Service name")
    status: str = Field(..., description="Service status")
    last_check: datetime = Field(..., description="Last status check timestamp")
    details: Optional[dict] = Field(None, description="Additional status details")
