from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from .enums import BookingStatus

class BookingModification(BaseModel):
    """Model for booking modification request - matches swagger /api/bookings/{booking_id}/modify"""
    new_booking_date: Optional[datetime] = Field(None, description="New booking date")
    modification_reason: Optional[str] = Field(None, description="Reason for modification")
    additional_services: Optional[List[str]] = Field(None, description="Additional services to add")

class BookingStatusResponse(BaseModel):
    """Response model for booking status - matches swagger /api/bookings/{booking_id}/status"""
    booking_id: int = Field(..., description="Booking ID")
    status: BookingStatus = Field(..., description="Current booking status")
    status_details: Optional[str] = Field(None, description="Additional status details")
    last_updated: datetime = Field(..., description="Last status update timestamp")

# Removed extensive booking models that aren't in swagger:
# - Booking entity model (no GET /api/bookings endpoint)
# - HotelSearchRequest, HotelBookingRequest (these are under /offers/ not /api/)
# - FlightSearchRequest, FlightBookingRequest (these are under /offers/ not /api/)
# - TravelPackageSearchRequest (this is under /offers/ not /api/)

# Note: The hotel/flight/travel search and booking are part of the integration
# services under /offers/ endpoints, not core booking management
