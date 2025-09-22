from fastmcp import FastMCP
from fastapi import Query, Path
from typing import Optional
from models import (
    ProfileHistoryResponse, CustomerProfileHistoryResponse, api_client
)

def register_profile_history_tools(mcp: FastMCP):
    """Register profile history-related MCP tools"""

    @mcp.tool(
        name="list_profile_history",
        description="Retrieve comprehensive customer profile history across the system with advanced filtering by customer, merchant, and date ranges. Returns detailed transaction history including offers utilized, discounts applied, savings achieved, and spending patterns for business intelligence and customer behavior analysis.",
        tags={"profile_history", "analytics", "customer_behavior", "transaction_history", "business_intelligence"},
        meta={"version": "1.0", "category": "analytics_reporting"}
    )
    async def list_profile_history(
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of records per page"),
        customer_id: Optional[int] = Query(None, description="Filter history by specific customer ID"),
        merchant_id: Optional[int] = Query(None, description="Filter history by specific merchant ID"),
        start_date: Optional[str] = Query(None, description="Filter history from this date (YYYY-MM-DD format)"),
        end_date: Optional[str] = Query(None, description="Filter history until this date (YYYY-MM-DD format)")
    ) -> dict:
        """List profile history with filtering options"""
        params = {"page": page, "per_page": per_page}
        if customer_id:
            params["customer_id"] = customer_id
        if merchant_id:
            params["merchant_id"] = merchant_id
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return await api_client.get("/api/profile-history", params=params)

    @mcp.tool(
        name="get_customer_profile_history",
        description="Generate a detailed profile history report for a specific customer including all transactions, offers utilized, total savings achieved, spending patterns, and reward accumulation. Provides comprehensive customer journey analysis with financial summaries for personalized service and targeted marketing.",
        tags={"profile_history", "customer_analytics", "financial_summary", "savings_tracking", "personalization"},
        meta={"version": "1.0", "category": "customer_analytics"}
    )
    async def get_customer_profile_history(
        customer_id: int = Path(..., description="Unique customer identifier to generate profile history for")
    ) -> dict:
        """Get profile history for a specific customer"""
        return await api_client.get(f"/api/customers/{customer_id}/profile-history")
