from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    Offer, OfferCreate, OfferUpdate, OfferListResponse, OfferActivationRequest,
    OfferActivation, OfferCategoriesResponse, api_client, OfferCategory
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
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of offers per page"),
        category: Optional[OfferCategory] = Query(None, description="Filter offers by category"),
        merchant_id: Optional[int] = Query(None, description="Filter offers by specific merchant ID"),
        is_active: Optional[bool] = Query(None, description="Filter by offer active status"),
        customer_id: Optional[int] = Query(None, description="Include customer-specific offer data")
    ) -> dict:
        """List available offers with filtering options"""
        params = {"page": page, "per_page": per_page}
        if category:
            params["category"] = category.value
        if merchant_id:
            params["merchant_id"] = merchant_id
        if is_active is not None:
            params["is_active"] = is_active
        if customer_id:
            params["customer_id"] = customer_id

        return await api_client.get("/api/offers", params=params)

    @mcp.tool(
        name="create_offer",
        description="Create a new promotional offer with comprehensive details including discount percentages, reward points, validity periods, merchant associations, and terms & conditions. Supports various offer types for targeted marketing campaigns and customer engagement.",
        tags={"offers", "promotions", "campaign_creation", "marketing", "discounts"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def create_offer(offer: OfferCreate = Body(..., description="Complete offer details including title, description, discount terms, validity period, and merchant association")) -> dict:
        """Create a new offer"""
        offer_data = offer.model_dump(exclude_unset=True)
        if offer_data.get("category"):
            offer_data["category"] = offer_data["category"].value if hasattr(offer_data["category"], "value") else offer_data["category"]
        return await api_client.post("/api/offers", data=offer_data)

    @mcp.tool(
        name="get_offer",
        description="Retrieve detailed information about a specific offer including statistics, activation data, and merchant details. Provides comprehensive offer analytics for performance monitoring and customer insights.",
        tags={"offers", "details", "analytics", "performance"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def get_offer(offer_id: int = Path(..., description="Offer ID to retrieve")) -> dict:
        """Get detailed information about a specific offer"""
        return await api_client.get(f"/api/offers/{offer_id}")

    @mcp.tool(
        name="update_offer",
        description="Update an existing promotional offer with new details, terms, or status. Allows modification of discount percentages, validity periods, merchant associations, and activation status for ongoing campaign optimization.",
        tags={"offers", "update", "campaign_management", "optimization"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def update_offer(
        offer_id: int = Path(..., description="Offer ID to update"),
        offer: OfferUpdate = Body(..., description="Updated offer details")
    ) -> dict:
        """Update an existing offer"""
        offer_data = offer.model_dump(exclude_unset=True)
        if offer_data.get("category"):
            offer_data["category"] = offer_data["category"].value if hasattr(offer_data["category"], "value") else offer_data["category"]
        return await api_client.put(f"/api/offers/{offer_id}", data=offer_data)

    @mcp.tool(
        name="delete_offer",
        description="Delete an offer from the system (only allowed if no active customer activations exist). Permanently removes the offer and all associated data for system cleanup and offer lifecycle management.",
        tags={"offers", "delete", "cleanup", "lifecycle"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def delete_offer(offer_id: int = Path(..., description="Offer ID to delete")) -> dict:
        """Delete an offer"""
        return await api_client.delete(f"/api/offers/{offer_id}")

    @mcp.tool(
        name="activate_offer_for_customer",
        description="Activate a specific promotional offer for a customer, enabling them to use the discount or earn rewards on qualifying transactions. Manages offer eligibility, customer enrollment, and tracks offer utilization for analytics and reporting.",
        tags={"offers", "activation", "customer_enrollment", "promotions"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def activate_offer_for_customer(
        offer_id: int = Path(..., description="Offer ID to activate"),
        activation: OfferActivationRequest = Body(..., description="Customer activation details")
    ) -> dict:
        """Activate an offer for a specific customer"""
        activation_data = activation.model_dump()
        return await api_client.post(f"/api/offers/{offer_id}/activate", data=activation_data)

    @mcp.tool(
        name="deactivate_offer",
        description="Deactivate an offer by setting its active status to false. Stops new customer activations while preserving existing activations for ongoing transaction processing and analytics.",
        tags={"offers", "deactivate", "status_management"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def deactivate_offer(offer_id: int = Path(..., description="Offer ID to deactivate")) -> dict:
        """Deactivate an offer"""
        return await api_client.post(f"/api/offers/{offer_id}/deactivate")

    @mcp.tool(
        name="reactivate_offer",
        description="Reactivate a previously deactivated offer (only if not expired). Enables new customer activations and restores offer availability for promotional campaigns.",
        tags={"offers", "reactivate", "status_management", "campaigns"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def reactivate_offer(offer_id: int = Path(..., description="Offer ID to reactivate")) -> dict:
        """Reactivate a deactivated offer"""
        return await api_client.post(f"/api/offers/{offer_id}/reactivate")

    @mcp.tool(
        name="expire_offer",
        description="Manually expire an offer by setting its expiry date to current time and deactivating it. Immediately stops all offer availability and customer activations for emergency campaign termination.",
        tags={"offers", "expire", "emergency", "termination"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def expire_offer(offer_id: int = Path(..., description="Offer ID to expire")) -> dict:
        """Manually expire an offer"""
        return await api_client.post(f"/api/offers/{offer_id}/expire")

    @mcp.tool(
        name="get_offer_categories",
        description="Retrieve all available offer categories with descriptions for campaign planning and offer categorization. Provides standardized category options for consistent offer classification and filtering.",
        tags={"offers", "categories", "classification", "planning"},
        meta={"version": "1.0", "category": "offer_management"}
    )
    async def get_offer_categories() -> dict:
        """Get all available offer categories"""
        return await api_client.get("/api/offers/categories")
