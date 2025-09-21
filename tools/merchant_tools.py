from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from datetime import datetime
from models import (
    Merchant, MerchantCreate, MerchantListResponse, MerchantAnalyticsResponse
)

def register_merchant_tools(mcp: FastMCP):
    """Register merchant-related MCP tools"""

    @mcp.tool(
        name="list_merchants",
        description="Retrieve a paginated list of all merchants in the system with optional filtering by category and active status. Supports pagination and returns merchant details including business information and activity status.",
        tags={"merchants", "catalog", "business"},
        meta={"version": "1.0", "category": "merchant_management"}
    )
    async def list_merchants(
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of merchants per page"),
        category: Optional[str] = Query(None, description="Filter by merchant category (RESTAURANT, RETAIL_STORE, etc.)"),
        is_active: Optional[bool] = Query(None, description="Filter by merchant active status")
    ) -> MerchantListResponse:
        """List all merchants with filtering options"""
        # Stub implementation - replace with actual database logic
        return MerchantListResponse(merchants=[], total=0)

    @mcp.tool(
        name="create_merchant",
        description="Register a new merchant in the system with business details including name, category, contact information, and address. Creates a unique merchant account for payment processing and offers.",
        tags={"merchants", "registration", "business"},
        meta={"version": "1.0", "category": "merchant_management"}
    )
    async def create_merchant(merchant: MerchantCreate = Body(...)) -> Merchant:
        """Create a new merchant account"""
        # Stub implementation - replace with actual database logic
        return Merchant(
            id=1,
            merchant_id=merchant.merchant_id,
            name=merchant.name,
            category=merchant.category,
            description=merchant.description,
            created_at=datetime.utcnow()
        )

    @mcp.tool(
        name="get_merchant_details",
        description="Retrieve detailed information about a specific merchant including business profile, contact details, category, and registration information. Used for merchant profile management.",
        tags={"merchants", "profile", "details"},
        meta={"version": "1.0", "category": "merchant_management"}
    )
    async def get_merchant_details(merchant_id: int = Path(..., description="Unique merchant identifier")) -> Merchant:
        """Get detailed information about a specific merchant"""
        # Stub implementation - replace with actual database logic
        return Merchant(
            id=merchant_id,
            merchant_id="MERCH001",
            name="Sample Merchant",
            category="RESTAURANT",
            description="A sample restaurant",
            created_at=datetime.utcnow()
        )

    @mcp.tool(
        name="get_merchant_analytics",
        description="Generate comprehensive analytics report for a merchant including total transactions, revenue, discounts provided, and active offers. Provides business insights for merchant performance tracking.",
        tags={"merchants", "analytics", "reporting", "business_intelligence"},
        meta={"version": "1.0", "category": "merchant_analytics"}
    )
    async def get_merchant_analytics(
        merchant_id: int = Path(..., description="Unique merchant identifier for analytics")
    ) -> MerchantAnalyticsResponse:
        """Get analytics data for a specific merchant"""
        # Stub implementation - replace with actual database logic
        return MerchantAnalyticsResponse(
            total_transactions=0,
            total_amount=0.0,
            total_discounts=0.0,
            active_offers=0
        )
