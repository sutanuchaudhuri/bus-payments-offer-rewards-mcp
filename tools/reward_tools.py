from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    Reward, RewardCreate, RewardListResponse, CustomerBalance, RedeemPointsRequest,
    RewardRedemption, RedemptionHistory, RewardStatus, api_client
)

def register_reward_tools(mcp: FastMCP):
    """Register reward-related MCP tools"""

    @mcp.tool(
        name="get_customer_rewards",
        description="Retrieve a comprehensive list of all rewards earned by a specific customer including points from transactions, offer bonuses, and promotional rewards. Returns detailed reward history with earning dates, sources, expiry information, and redemption status for loyalty program management.",
        tags={"rewards", "loyalty_program", "customer_benefits", "points_tracking"},
        meta={"version": "1.0", "category": "rewards_management"}
    )
    async def get_customer_rewards(
        customer_id: int = Path(..., description="Unique customer identifier to retrieve rewards for"),
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of rewards per page"),
        status: Optional[RewardStatus] = Query(None, description="Filter by reward status")
    ) -> dict:
        """Get all rewards for a specific customer - matches swagger GET /api/rewards/customer/{customer_id}"""
        params = {"page": page, "per_page": per_page}
        if status:
            # Convert enum to string for API compatibility
            params["status"] = str(status.value) if hasattr(status, 'value') else str(status)
        return await api_client.get(f"/api/rewards/customer/{customer_id}", params=params)

    @mcp.tool(
        name="create_reward",
        description="Manually create a reward for a customer with specified points, description, and optional offer association. Used for promotional rewards, manual adjustments, and special recognition programs with full audit trail and expiry management.",
        tags={"rewards", "manual_creation", "promotions", "administration"},
        meta={"version": "1.0", "category": "rewards_management"}
    )
    async def create_reward(reward: RewardCreate = Body(..., description="Reward creation details including customer, points, description, and optional offer association")) -> dict:
        """Create a new reward manually"""
        reward_data = reward.model_dump(exclude_unset=True)
        return await api_client.post("/api/rewards", data=reward_data)

    @mcp.tool(
        name="get_reward_details",
        description="Retrieve detailed information about a specific reward including points earned, source transaction, offer association, earning date, expiry date, and redemption status for comprehensive reward tracking and customer service.",
        tags={"rewards", "details", "tracking", "customer_service"},
        meta={"version": "1.0", "category": "rewards_management"}
    )
    async def get_reward_details(reward_id: int = Path(..., description="Reward ID to retrieve details for")) -> dict:
        """Get detailed reward information"""
        return await api_client.get(f"/api/rewards/{reward_id}")

    @mcp.tool(
        name="get_customer_reward_balance",
        description="Calculate and return the current reward point balance for a customer including total points earned, available points for redemption, redeemed points, pending points, expired points, and current dollar value for comprehensive loyalty program status.",
        tags={"rewards", "balance_inquiry", "loyalty_program", "points_valuation"},
        meta={"version": "1.0", "category": "rewards_management"}
    )
    async def get_customer_reward_balance(customer_id: int = Path(..., description="Unique customer identifier to check reward balance for")) -> dict:
        """Get the current reward point balance for a customer"""
        return await api_client.get(f"/api/customers/{customer_id}/rewards/balance")

    @mcp.tool(
        name="redeem_points",
        description="Process reward point redemption for a customer, converting loyalty points to cash value or benefits. Validates point availability, processes redemption transaction, updates customer balance, and generates redemption confirmation for reward program administration.",
        tags={"rewards", "redemption", "loyalty_program", "points_conversion", "customer_benefits"},
        meta={"version": "1.0", "category": "rewards_management"}
    )
    async def redeem_points(
        customer_id: int = Path(..., description="Unique customer identifier for point redemption"),
        request: RedeemPointsRequest = Body(..., description="Redemption request with points amount and optional description")
    ) -> dict:
        """Redeem reward points for a customer"""
        request_data = request.model_dump(exclude_unset=True)
        return await api_client.post(f"/api/customers/{customer_id}/rewards/redeem", data=request_data)

    @mcp.tool(
        name="redeem_specific_reward",
        description="Redeem points from a specific reward entry, allowing partial or full redemption with automatic balance updates and transaction tracking. Provides granular control over reward utilization and maintains detailed redemption history.",
        tags={"rewards", "specific_redemption", "granular_control", "tracking"},
        meta={"version": "1.0", "category": "rewards_management"}
    )
    async def redeem_specific_reward(
        reward_id: int = Path(..., description="Specific reward ID to redeem from"),
        redemption: RewardRedemption = Body(..., description="Redemption details including optional points amount")
    ) -> dict:
        """Redeem points from a specific reward"""
        redemption_data = redemption.model_dump(exclude_unset=True)
        return await api_client.post(f"/api/rewards/{reward_id}/redeem", data=redemption_data)

    @mcp.tool(
        name="get_redemption_history",
        description="Retrieve comprehensive redemption history for a customer including all point redemptions, dates, amounts, descriptions, and current status with date range filtering. Provides complete audit trail of loyalty program utilization for customer service and analytics.",
        tags={"rewards", "redemption_history", "audit_trail", "customer_service"},
        meta={"version": "1.0", "category": "rewards_management"}
    )
    async def get_redemption_history(
        customer_id: int = Path(..., description="Customer ID to retrieve redemption history for"),
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of redemptions per page"),
        start_date: Optional[str] = Query(None, description="Filter redemptions from this date (ISO format)"),
        end_date: Optional[str] = Query(None, description="Filter redemptions until this date (ISO format)")
    ) -> dict:
        """Get customer's redemption history with date filtering - matches swagger GET /api/rewards/customer/{customer_id}/history"""
        params = {"page": page, "per_page": per_page}
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        return await api_client.get(f"/api/rewards/customer/{customer_id}/history", params=params)
