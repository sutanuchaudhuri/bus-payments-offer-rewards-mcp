from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    Booking, BookingModification, BookingStatusResponse, HotelSearchRequest,
    HotelBookingRequest, FlightSearchRequest, FlightBookingRequest,
    TravelPackageSearchRequest, BookingStatus, api_client
)

def register_booking_tools(mcp: FastMCP):
    """Register booking-related MCP tools"""

    @mcp.tool(
        name="modify_booking",
        description="Modify an existing booking with new dates, services, or other details. Handles availability checking, price adjustments, and customer notifications with full change tracking and confirmation workflow.",
        tags={"bookings", "modifications", "customer_service", "travel_changes"},
        meta={"version": "1.0", "category": "booking_management"}
    )
    async def modify_booking(
        booking_id: int = Path(..., description="Booking ID to modify"),
        modification: BookingModification = Body(..., description="Booking modification details including new dates, services, and reason")
    ) -> dict:
        """Modify an existing booking"""
        modification_data = modification.model_dump(exclude_unset=True)
        return await api_client.put(f"/api/bookings/{booking_id}/modify", data=modification_data)

    @mcp.tool(
        name="get_booking_status",
        description="Check the current status of a specific booking including confirmation status, payment status, and any recent updates. Provides real-time booking information for customer inquiries and service management.",
        tags={"bookings", "status_check", "customer_service", "tracking"},
        meta={"version": "1.0", "category": "booking_management"}
    )
    async def get_booking_status(booking_id: int = Path(..., description="Booking ID to check status for")) -> dict:
        """Get booking status"""
        return await api_client.get(f"/api/bookings/{booking_id}/status")

    @mcp.tool(
        name="search_hotels",
        description="Search for available hotels based on location, dates, and occupancy requirements. Returns hotel options with pricing, amenities, availability, and booking details for travel planning and reservation services.",
        tags={"travel", "hotels", "search", "accommodations"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def search_hotels(search: HotelSearchRequest = Body(..., description="Hotel search criteria including city, dates, rooms, and guests")) -> dict:
        """Search for available hotels"""
        search_data = search.model_dump(exclude_unset=True)
        return await api_client.post("/offers/hotel/search-hotels", data=search_data)

    @mcp.tool(
        name="book_hotel",
        description="Create a hotel booking with guest information, room requirements, and payment details. Processes reservation confirmation, handles payment authorization, and provides booking confirmation with full itinerary details.",
        tags={"travel", "hotels", "booking", "reservations"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def book_hotel(booking: HotelBookingRequest = Body(..., description="Hotel booking details including hotel, customer, dates, and guest information")) -> dict:
        """Book a hotel"""
        booking_data = booking.model_dump(exclude_unset=True)
        return await api_client.post("/offers/hotel/book-hotel", data=booking_data)

    @mcp.tool(
        name="get_hotel_booking_details",
        description="Retrieve detailed information about a specific hotel booking including confirmation details, guest information, and booking status for customer service and travel management.",
        tags={"travel", "hotels", "booking_details", "customer_service"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def get_hotel_booking_details(booking_reference: str = Path(..., description="Hotel booking reference")) -> dict:
        """Get hotel booking details"""
        return await api_client.get(f"/offers/hotel/booking/{booking_reference}")

    @mcp.tool(
        name="get_available_cities",
        description="Retrieve list of available cities for hotel bookings. Provides destination options for travel planning and hotel search functionality with city-specific information.",
        tags={"travel", "hotels", "cities", "destinations"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def get_available_cities() -> dict:
        """Get available cities for hotel bookings"""
        return await api_client.get("/offers/hotel/cities")

    @mcp.tool(
        name="search_flights",
        description="Search for available flights based on origin, destination, dates, and passenger count. Returns flight options with schedules, pricing, airlines, and booking availability for travel planning and flight reservations.",
        tags={"travel", "flights", "search", "airlines"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def search_flights(search: FlightSearchRequest = Body(..., description="Flight search criteria including origin, destination, dates, and passengers")) -> dict:
        """Search for available flights"""
        search_data = search.model_dump(exclude_unset=True)
        return await api_client.post("/offers/travel/search-flights", data=search_data)

    @mcp.tool(
        name="book_flight",
        description="Create a flight booking with passenger information and payment details. Processes seat reservations, handles payment authorization, and provides booking confirmation with e-tickets and itinerary information.",
        tags={"travel", "flights", "booking", "airlines"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def book_flight(booking: FlightBookingRequest = Body(..., description="Flight booking details including flight, customer, and passenger information")) -> dict:
        """Book a flight"""
        booking_data = booking.model_dump(exclude_unset=True)
        return await api_client.post("/offers/travel/book-flight", data=booking_data)

    @mcp.tool(
        name="get_flight_booking_details",
        description="Retrieve detailed information about a specific flight booking including ticket details, passenger information, and flight status for customer service and travel management.",
        tags={"travel", "flights", "booking_details", "customer_service"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def get_flight_booking_details(booking_reference: str = Path(..., description="Flight booking reference")) -> dict:
        """Get flight booking details"""
        return await api_client.get(f"/offers/travel/booking/{booking_reference}")

    @mcp.tool(
        name="get_available_airports",
        description="Retrieve list of available airports for flight bookings. Provides airport codes and information for flight search functionality and travel planning with comprehensive airport data.",
        tags={"travel", "flights", "airports", "destinations"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def get_available_airports() -> dict:
        """Get available airports for flight bookings"""
        return await api_client.get("/offers/travel/airports")

    @mcp.tool(
        name="search_travel_packages",
        description="Search for comprehensive travel packages including flights, hotels, and activities based on destination, dates, and traveler requirements. Returns package options with bundled pricing and complete itinerary details.",
        tags={"travel", "packages", "search", "vacation_planning"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def search_travel_packages(search: TravelPackageSearchRequest = Body(..., description="Travel package search criteria including destinations, dates, and traveler preferences")) -> dict:
        """Search for travel packages"""
        search_data = search.model_dump(exclude_unset=True)
        return await api_client.post("/offers/search/travel-package", data=search_data)
