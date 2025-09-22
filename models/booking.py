from datetime import datetime
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from .enums import BookingStatus

class BookingModification(BaseModel):
    """Model for booking modification request"""
    new_booking_date: Optional[datetime] = Field(None, description="New booking date")
    modification_reason: Optional[str] = Field(None, description="Reason for modification")
    additional_services: Optional[List[str]] = Field(None, description="Additional services to add")

class Booking(BaseModel):
    """Model for booking entity"""
    id: int = Field(..., description="Booking ID")
    customer_id: int = Field(..., description="Customer ID")
    booking_date: datetime = Field(..., description="Booking date")
    status: BookingStatus = Field(..., description="Booking status")
    total_amount: float = Field(..., description="Total booking amount")
    services: Optional[List[str]] = Field(None, description="Booked services")
    created_at: datetime = Field(..., description="Creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")

class BookingStatusResponse(BaseModel):
    """Response model for booking status"""
    booking_id: int = Field(..., description="Booking ID")
    status: BookingStatus = Field(..., description="Current booking status")
    status_details: Optional[str] = Field(None, description="Additional status details")
    last_updated: datetime = Field(..., description="Last status update timestamp")

class HotelSearchRequest(BaseModel):
    """Model for hotel search request"""
    city: str = Field(..., description="City to search hotels in")
    check_in: str = Field(..., description="Check-in date (YYYY-MM-DD)")
    check_out: str = Field(..., description="Check-out date (YYYY-MM-DD)")
    rooms: int = Field(1, description="Number of rooms", ge=1)
    guests: int = Field(1, description="Number of guests", ge=1)

class HotelBookingRequest(BaseModel):
    """Model for hotel booking request"""
    hotel_id: str = Field(..., description="Hotel ID")
    customer_id: int = Field(..., description="Customer ID")
    check_in: str = Field(..., description="Check-in date (YYYY-MM-DD)")
    check_out: str = Field(..., description="Check-out date (YYYY-MM-DD)")
    rooms: int = Field(1, description="Number of rooms", ge=1)
    guests: List[Dict[str, Any]] = Field(..., description="Guest information")

class FlightSearchRequest(BaseModel):
    """Model for flight search request"""
    origin: str = Field(..., description="Origin airport code")
    destination: str = Field(..., description="Destination airport code")
    departure_date: str = Field(..., description="Departure date (YYYY-MM-DD)")
    return_date: Optional[str] = Field(None, description="Return date (YYYY-MM-DD)")
    passengers: int = Field(1, description="Number of passengers", ge=1)

class FlightBookingRequest(BaseModel):
    """Model for flight booking request"""
    flight_id: str = Field(..., description="Flight ID")
    customer_id: int = Field(..., description="Customer ID")
    passengers: List[Dict[str, Any]] = Field(..., description="Passenger information")

class TravelPackageSearchRequest(BaseModel):
    """Model for travel package search request"""
    origin: str = Field(..., description="Origin location")
    destination: str = Field(..., description="Destination location")
    departure_date: str = Field(..., description="Departure date (YYYY-MM-DD)")
    return_date: str = Field(..., description="Return date (YYYY-MM-DD)")
    passengers: Optional[int] = Field(1, description="Number of passengers", ge=1)
    rooms: Optional[int] = Field(1, description="Number of rooms", ge=1)
