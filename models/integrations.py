from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

# Token models - based on swagger /api/tokens/* endpoints
class CardTokenRequest(BaseModel):
    """Model for creating a card token - matches swagger /api/tokens/create"""
    card_id: int = Field(..., description="Credit card ID")
    token_type: str = Field("SINGLE_USE", description="Type of token: SINGLE_USE, MULTI_USE, RECURRING")
    expires_in_hours: int = Field(24, description="Token expiry in hours", ge=1, le=8760)

class CardToken(BaseModel):
    """Model for card token entity - based on swagger responses"""
    id: str = Field(..., description="Token ID")
    card_id: int = Field(..., description="Associated credit card ID")
    customer_id: int = Field(..., description="Customer ID")
    token_type: str = Field(..., description="Token type")
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

# Travel integration models - based on swagger /offers/ endpoints
class HotelSearchRequest(BaseModel):
    """Model for hotel search - matches swagger /offers/hotel/search-hotels"""
    city: str = Field(..., description="City to search hotels in")
    check_in: str = Field(..., description="Check-in date (YYYY-MM-DD)")
    check_out: str = Field(..., description="Check-out date (YYYY-MM-DD)")
    rooms: int = Field(1, description="Number of rooms", ge=1)
    guests: int = Field(1, description="Number of guests", ge=1)

class HotelBookingRequest(BaseModel):
    """Model for hotel booking - matches swagger /offers/hotel/book-hotel"""
    hotel_id: str = Field(..., description="Hotel ID")
    customer_id: int = Field(..., description="Customer ID")
    check_in: str = Field(..., description="Check-in date (YYYY-MM-DD)")
    check_out: str = Field(..., description="Check-out date (YYYY-MM-DD)")
    rooms: int = Field(1, description="Number of rooms", ge=1)
    guests: List[Dict[str, Any]] = Field(..., description="Guest information")

class FlightSearchRequest(BaseModel):
    """Model for flight search - matches swagger /offers/travel/search-flights"""
    origin: str = Field(..., description="Origin airport code")
    destination: str = Field(..., description="Destination airport code")
    departure_date: str = Field(..., description="Departure date (YYYY-MM-DD)")
    return_date: Optional[str] = Field(None, description="Return date (YYYY-MM-DD)")
    passengers: int = Field(1, description="Number of passengers", ge=1)

class FlightBookingRequest(BaseModel):
    """Model for flight booking - matches swagger /offers/travel/book-flight"""
    flight_id: str = Field(..., description="Flight ID")
    customer_id: int = Field(..., description="Customer ID")
    passengers: List[Dict[str, Any]] = Field(..., description="Passenger information")

class TravelPackageSearchRequest(BaseModel):
    """Model for travel package search - matches swagger /offers/search/travel-package"""
    origin: str = Field(..., description="Origin location")
    destination: str = Field(..., description="Destination location")
    departure_date: str = Field(..., description="Departure date (YYYY-MM-DD)")
    return_date: str = Field(..., description="Return date (YYYY-MM-DD)")
    passengers: Optional[int] = Field(1, description="Number of passengers", ge=1)
    rooms: Optional[int] = Field(1, description="Number of rooms", ge=1)

# Shopping integration models - based on swagger /offers/shopping/* endpoints
class ShoppingProductSearch(BaseModel):
    """Model for shopping product search - matches swagger /offers/shopping/search"""
    query: Optional[str] = Field(None, description="Search query")
    category: Optional[str] = Field(None, description="Product category")
    brand: Optional[str] = Field(None, description="Product brand")
    min_price: Optional[float] = Field(None, description="Minimum price", ge=0)
    max_price: Optional[float] = Field(None, description="Maximum price", ge=0)
    page: int = Field(1, description="Page number", ge=1)
    per_page: int = Field(20, description="Items per page", ge=1, le=100)

class ShoppingCartItem(BaseModel):
    """Model for adding item to cart - matches swagger /offers/shopping/add-to-cart"""
    customer_id: int = Field(..., description="Customer ID")
    product_id: str = Field(..., description="Product ID")
    quantity: int = Field(1, description="Quantity", ge=1)

class ShoppingOrder(BaseModel):
    """Model for creating shopping order - matches swagger /offers/shopping/create-order"""
    customer_id: int = Field(..., description="Customer ID")
    shipping_address: dict = Field(..., description="Shipping address details")
    payment_method: str = Field(..., description="Payment method: credit_card or points")

# System integration status
class IntegrationStatus(BaseModel):
    """Model for integration status - matches swagger /simulator/status"""
    service: str = Field(..., description="Service name")
    status: str = Field(..., description="Service status")
    last_check: datetime = Field(..., description="Last status check timestamp")
    details: Optional[dict] = Field(None, description="Additional status details")
