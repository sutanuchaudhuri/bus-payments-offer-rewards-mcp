from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    Offer, OfferCreate, OfferListResponse, OfferActivationRequest
)

def register_offer_tools(mcp: FastMCP):
    """Register offer-related MCP tools"""

    @mcp.tool(
        name="list_offers",
        description="Retrieve a comprehensive catalog of available promotional offers with filtering by category, merchant, and active status. Returns detailed offer information including discount percentages, reward points, validity periods, and merchant associations for customer targeting and campaign management.",
        tags={"offers", "promotions", "discounts", "marketing", "rewards"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def list_offers(
        category: Optional[str] = Query(None, description="Filter offers by category (RESTAURANT, RETAIL_STORE, etc.)"),
        merchant_id: Optional[int] = Query(None, description="Filter offers by specific merchant ID"),
        is_active: Optional[bool] = Query(None, description="Filter by offer active status")
    ) -> OfferListResponse:
        """List available offers with filtering options"""
        # Stub implementation - replace with actual database logic
        return OfferListResponse(offers=[])

    @mcp.tool(
        name="create_offer",
        description="Create a new promotional offer with comprehensive details including discount percentages, reward points, validity periods, merchant associations, and terms & conditions. Supports various offer types for targeted marketing campaigns and customer engagement.",
        tags={"offers", "promotions", "campaign_creation", "marketing", "discounts"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def create_offer(offer: OfferCreate = Body(..., description="Complete offer details including title, description, discount terms, validity period, and merchant association")) -> Offer:
        """Create a new offer"""
        # Stub implementation - replace with actual database logic
        return Offer(
            id=1,
            title=offer.title,
            description=offer.description,
            category=offer.category,
            merchant_id=offer.merchant_id,
            discount_percentage=offer.discount_percentage,
            start_date=offer.start_date,
            expiry_date=offer.expiry_date,
            is_active=True
        )

    @mcp.tool(
        name="activate_offer",
        description="Activate a specific promotional offer for a customer, enabling them to use the discount or earn rewards on qualifying transactions. Manages offer eligibility, customer enrollment, and tracks offer utilization for analytics and reporting.",
        tags={"offers", "activation", "customer_enrollment", "promotions"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def activate_offer(
        offer_id: int = Path(..., description="Unique identifier of the offer to activate"),
        request: OfferActivationRequest = Body(..., description="Customer activation request with customer ID")
    ) -> dict:
        """Activate an offer for a specific customer"""
        # Stub implementation - replace with actual database logic
        return {"message": "Offer activated successfully"}
