from fastmcp import FastMCP
from fastapi import Path, Body

from models import (
    RewardListResponse, RewardBalanceResponse, RedeemPointsRequest
)

def register_reward_tools(mcp: FastMCP):
    """Register reward-related MCP tools"""

    @mcp.tool(
        name="get_customer_rewards",
        description="Retrieve a comprehensive list of all rewards earned by a specific customer including points from transactions, offer bonuses, and promotional rewards. Returns detailed reward history with earning dates, sources, expiry information, and redemption status for loyalty program management.",
        tags={"rewards", "loyalty_program", "customer_benefits", "points_tracking"},
        meta={"version": "1.0", "category": "rewards_management"}
    )
    async def get_customer_rewards(customer_id: int = Path(..., description="Unique customer identifier to retrieve rewards for")) -> RewardListResponse:
        """Get all rewards for a specific customer"""
        # Stub implementation - replace with actual database logic
        return RewardListResponse(rewards=[])

    @mcp.tool(
        name="get_customer_reward_balance",
        description="Calculate and return the current reward point balance for a customer including total points earned, available points for redemption, expired points, and current dollar value. Provides real-time loyalty program status and redemption capacity analysis.",
        tags={"rewards", "balance_inquiry", "loyalty_program", "points_valuation"},
        meta={"version": "1.0", "category": "rewards_management"}
    )
    async def get_customer_reward_balance(
        customer_id: int = Path(..., description="Unique customer identifier to check reward balance for")
    ) -> RewardBalanceResponse:
        """Get the current reward point balance for a customer"""
        # Stub implementation - replace with actual database logic
        return RewardBalanceResponse(
            total_points=0,
            available_points=0,
            dollar_value=0.0
        )

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
        # Stub implementation - replace with actual database logic
        return {"message": "Points redeemed successfully"}
