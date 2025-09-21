from fastmcp import FastMCP
from fastapi import Path, Body
from models import CreditCardCreate

def register_credit_card_tools(mcp: FastMCP):
    """Register credit card-related MCP tools"""

    @mcp.tool(
        name="add_credit_card",
        description="Add a new credit card to a customer's account with complete card details including number, holder name, expiry date, product type, and credit limit. Supports multiple card types (PLATINUM, GOLD, SILVER, BASIC) and validates card information.",
        tags={"credit_cards", "payment_methods", "card_management", "customer_accounts"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def add_credit_card(
        customer_id: int = Path(..., description="Unique customer identifier to associate the credit card with"),
        card: CreditCardCreate = Body(..., description="Credit card details including number, holder name, expiry, and limits")
    ) -> dict:
        """Add a new credit card to customer account"""
        # Stub implementation - replace with actual database logic
        return {"message": "Credit card added successfully", "card_id": 1}
