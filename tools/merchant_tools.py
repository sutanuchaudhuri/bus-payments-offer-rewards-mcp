from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
import os
from models import (
    Merchant, MerchantCreate, MerchantUpdate, MerchantListResponse,
    MerchantAnalytics, MerchantCategoriesResponse, MerchantCategory, api_client
)

def register_merchant_tools(mcp: FastMCP):
    """Register merchant-related MCP tools"""

    # Read admin tools enabled setting from environment
    admin_tools_enabled = os.getenv("ADMIN_TOOLS_ENABLED", "false").lower() == "true"

    @mcp.tool(
        name="list_merchants",
        description="Retrieve a paginated list of all merchants in the system with optional filtering by category and active status. Supports pagination and returns merchant details including business information, contact details, and activity status for comprehensive merchant management.",
        tags={"merchants", "catalog", "business", "search"},
        meta={"version": "1.0", "category": "merchant_management"},

    )
    async def list_merchants(
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of merchants per page"),
        category: Optional[MerchantCategory] = Query(None, description="Filter by merchant category"),
        is_active: Optional[bool] = Query(None, description="Filter by merchant active status")
    ) -> dict:
        """List all merchants with filtering options"""
        params = {"page": page, "per_page": per_page}
        if category:
            # Convert enum to string for API compatibility
            params["category"] = category.value if hasattr(category, 'value') else str(category)
        if is_active is not None:
            params["is_active"] = is_active
        return await api_client.get("/api/merchants", params=params)

    @mcp.tool(
        name="create_merchant",
        description="Register a new merchant in the system with comprehensive business details including name, category, contact information, website, and address. Creates a unique merchant account for payment processing, offer management, and transaction tracking.",
        tags={"merchants", "registration", "business", "onboarding"},
        meta={"version": "1.0", "category": "merchant_management"},
        enabled=admin_tools_enabled
    )
    async def create_merchant(merchant: MerchantCreate = Body(..., description="Complete merchant registration details including business name, category, contact information, and operational details")) -> dict:
        """Create a new merchant account"""
        merchant_data = merchant.model_dump(exclude_unset=True)
        if merchant_data.get("category"):
            merchant_data["category"] = merchant_data["category"].value if hasattr(merchant_data["category"], "value") else merchant_data["category"]
        return await api_client.post("/api/merchants", data=merchant_data)

    @mcp.tool(
        name="get_merchant_details",
        description="Retrieve detailed information about a specific merchant including business profile, contact details, category, registration information, and operational status. Used for merchant profile management and customer service.",
        tags={"merchants", "profile", "details", "support"},
        meta={"version": "1.0", "category": "merchant_management"}
    )
    async def get_merchant_details(merchant_id: int = Path(..., description="Merchant ID to retrieve")) -> dict:
        """Get detailed merchant information"""
        return await api_client.get(f"/api/merchants/{merchant_id}")

    @mcp.tool(
        name="update_merchant",
        description="Update existing merchant information including business name, category, contact details, website, and operational status. Supports partial updates while maintaining data integrity and business continuity.",
        tags={"merchants", "update", "profile_management", "business"},
        meta={"version": "1.0", "category": "merchant_management"},
        enabled=admin_tools_enabled
    )
    async def update_merchant(
        merchant_id: int = Path(..., description="Merchant ID to update"),
        merchant: MerchantUpdate = Body(..., description="Updated merchant information")
    ) -> dict:
        """Update merchant information"""
        merchant_data = merchant.model_dump(exclude_unset=True)
        if merchant_data.get("category"):
            merchant_data["category"] = merchant_data["category"].value if hasattr(merchant_data["category"], "value") else merchant_data["category"]
        return await api_client.put(f"/api/merchants/{merchant_id}", data=merchant_data)

    @mcp.tool(
        name="delete_merchant",
        description="Remove a merchant from the system. Permanently deletes merchant profile and associated data. Use with caution as this action cannot be undone and may affect related transactions and offers.",
        tags={"merchants", "deletion", "cleanup", "business"},
        meta={"version": "1.0", "category": "merchant_management"},
        enabled=admin_tools_enabled
    )
    async def delete_merchant(merchant_id: int = Path(..., description="Merchant ID to delete")) -> dict:
        """Delete a merchant"""
        return await api_client.delete(f"/api/merchants/{merchant_id}")

    @mcp.tool(
        name="get_merchant_categories",
        description="Retrieve all available merchant categories with descriptions for business classification and filtering. Provides standardized category options for consistent merchant categorization and search functionality.",
        tags={"merchants", "categories", "classification", "business"},
        meta={"version": "1.0", "category": "merchant_management"}
    )
    async def get_merchant_categories() -> dict:
        """Get all available merchant categories"""
        return await api_client.get("/api/merchants/categories")

    @mcp.tool(
        name="get_merchant_analytics",
        description="Retrieve comprehensive analytics data for a specific merchant including transaction volumes, amounts, offer usage statistics, and performance metrics over specified time periods for business intelligence and reporting.",
        tags={"merchants", "analytics", "reporting", "performance", "business_intelligence"},
        meta={"version": "1.0", "category": "merchant_management"},
        enabled=admin_tools_enabled
    )
    async def get_merchant_analytics(
        merchant_id: int = Path(..., description="Merchant ID for analytics"),
        period: Optional[str] = Query("month", description="Analytics period (day, week, month, year)")
    ) -> dict:
        """Get merchant analytics data"""
        params = {"period": period}
        return await api_client.get(f"/api/merchants/{merchant_id}/analytics", params=params)
