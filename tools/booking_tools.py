from fastmcp import FastMCP
from fastapi import Path, Body
from models import BookingModification, api_client

def register_booking_tools(mcp: FastMCP):
    """Register booking-related MCP tools - only 2 endpoints exist in swagger"""

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
        """Modify an existing booking - matches swagger PUT /api/bookings/{booking_id}/modify"""
        modification_data = modification.model_dump(exclude_unset=True)
        return await api_client.put(f"/api/bookings/{booking_id}/modify", data=modification_data)

    @mcp.tool(
        name="get_booking_status",
        description="Check the current status of a specific booking including confirmation status, payment status, and any recent updates. Provides real-time booking information for customer inquiries and service management.",
        tags={"bookings", "status_check", "customer_service", "tracking"},
        meta={"version": "1.0", "category": "booking_management"}
    )
    async def get_booking_status(booking_id: int = Path(..., description="Booking ID to check status for")) -> dict:
        """Get booking status - matches swagger GET /api/bookings/{booking_id}/status"""
        return await api_client.get(f"/api/bookings/{booking_id}/status")

# Removed all hotel/flight/travel tools - these are part of integration services
# under /offers/ endpoints and belong in integration_tools.py, not booking_tools.py
# The actual booking API only has 2 endpoints for modifying and checking status
