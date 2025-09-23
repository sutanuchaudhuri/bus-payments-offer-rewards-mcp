from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    CreditCard, CreditCardCreate, CreditCardUpdate, CreditCardListResponse,
    CreditCardProduct, api_client
)

def register_credit_card_tools(mcp: FastMCP):
    """Register credit card-related MCP tools - based on actual swagger endpoints"""

    @mcp.tool(
        name="list_customer_credit_cards",
        description="Retrieve a list of credit cards for a specific customer. Returns comprehensive card information including masked numbers, product types, credit limits, and activation status for account management.",
        tags={"credit_cards", "customer_accounts", "card_management"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def list_customer_credit_cards(
        customer_id: int = Path(..., description="Customer ID to list credit cards for")
    ) -> dict:
        """List credit cards for a customer - matches swagger GET /api/customers/{customer_id}/credit-cards"""
        return await api_client.get(f"/api/customers/{customer_id}/credit-cards")

    @mcp.tool(
        name="add_credit_card",
        description="Add a new credit card to a customer's account with complete card details including number, holder name, expiry date, product type, and credit limit. Supports multiple card types (PLATINUM, GOLD, SILVER, BASIC) with automatic validation and secure storage.",
        tags={"credit_cards", "payment_methods", "card_management", "customer_accounts"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def add_credit_card(
        customer_id: int = Path(..., description="Customer ID to associate the credit card with"),
        card: CreditCardCreate = Body(..., description="Credit card details including number, holder name, expiry, product type, and credit limits")
    ) -> dict:
        """Add a new credit card to customer account - matches swagger POST /api/customers/{customer_id}/credit-cards"""
        card_data = card.model_dump(exclude_unset=True)
        if card_data.get("product_type"):
            card_data["product_type"] = card_data["product_type"].value if hasattr(card_data["product_type"], "value") else card_data["product_type"]
        return await api_client.post(f"/api/customers/{customer_id}/credit-cards", data=card_data)

    @mcp.tool(
        name="update_credit_card",
        description="Update existing credit card information including holder name, expiry date, product type, credit limits, and activation status. Supports partial updates while maintaining security and data integrity for ongoing account management.",
        tags={"credit_cards", "card_management", "account_updates", "customer_service"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def update_credit_card(
        customer_id: int = Path(..., description="Customer ID"),
        card_id: int = Path(..., description="Credit card ID to update"),
        card: CreditCardUpdate = Body(..., description="Updated credit card information")
    ) -> dict:
        """Update credit card information - matches swagger PUT /api/customers/{customer_id}/credit-cards/{card_id}"""
        card_data = card.model_dump(exclude_unset=True)
        if card_data.get("product_type"):
            card_data["product_type"] = card_data["product_type"].value if hasattr(card_data["product_type"], "value") else card_data["product_type"]
        return await api_client.put(f"/api/customers/{customer_id}/credit-cards/{card_id}", data=card_data)

    @mcp.tool(
        name="delete_credit_card",
        description="Remove a credit card from the system. Permanently deletes card information and deactivates all associated payment capabilities. Use with caution as this action cannot be undone and may affect pending transactions.",
        tags={"credit_cards", "card_deletion", "account_management", "security"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def delete_credit_card(
        customer_id: int = Path(..., description="Customer ID"),
        card_id: int = Path(..., description="Credit card ID to delete")
    ) -> dict:
        """Delete a credit card - matches swagger DELETE /api/customers/{customer_id}/credit-cards/{card_id}"""
        return await api_client.delete(f"/api/customers/{customer_id}/credit-cards/{card_id}")

# Removed tools that don't exist in swagger:
# - get_credit_card_details (no standalone credit card GET endpoint)
# - activate_credit_card (no activation endpoint in swagger)
# - deactivate_credit_card (no deactivation endpoint in swagger)
