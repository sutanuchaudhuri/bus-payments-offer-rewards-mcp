from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    CreditCard, CreditCardCreate, CreditCardUpdate, CreditCardListResponse,
    CreditCardProduct, api_client
)

def register_credit_card_tools(mcp: FastMCP):
    """Register credit card-related MCP tools"""
    
    @mcp.tool(
        name="list_credit_cards",
        description="Retrieve a paginated list of credit cards for a specific customer with optional filtering by product type and active status. Returns comprehensive card information including masked numbers, product types, credit limits, and activation status for account management.",
        tags={"credit_cards", "customer_accounts", "card_management", "search"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def list_credit_cards(
        customer_id: int = Path(..., description="Customer ID to list credit cards for"),
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of cards per page"),
        product_type: Optional[CreditCardProduct] = Query(None, description="Filter by card product type"),
        is_active: Optional[bool] = Query(None, description="Filter by card active status")
    ) -> dict:
        """List credit cards for a customer"""
        params = {"page": page, "per_page": per_page}
        if product_type:
            params["product_type"] = product_type.value
        if is_active is not None:
            params["is_active"] = is_active
        return await api_client.get(f"/api/customers/{customer_id}/credit-cards", params=params)

    @mcp.tool(
        name="add_credit_card",
        description="Add a new credit card to a customer's account with complete card details including number, holder name, expiry date, product type, and credit limit. Supports multiple card types (PLATINUM, GOLD, SILVER, BASIC) with automatic validation and secure storage.",
        tags={"credit_cards", "payment_methods", "card_management", "customer_accounts"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def add_credit_card(
        customer_id: int = Path(..., description="Unique customer identifier to associate the credit card with"),
        card: CreditCardCreate = Body(..., description="Credit card details including number, holder name, expiry, product type, and credit limits")
    ) -> dict:
        """Add a new credit card to customer account"""
        card_data = card.model_dump(exclude_unset=True)
        if card_data.get("product_type"):
            card_data["product_type"] = card_data["product_type"].value if hasattr(card_data["product_type"], "value") else card_data["product_type"]
        return await api_client.post(f"/api/customers/{customer_id}/credit-cards", data=card_data)

    @mcp.tool(
        name="get_credit_card_details",
        description="Retrieve detailed information about a specific credit card including masked number, holder name, expiry date, product type, credit limits, available credit, and transaction history for comprehensive account management and customer service.",
        tags={"credit_cards", "card_details", "account_management", "customer_service"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def get_credit_card_details(card_id: int = Path(..., description="Credit card ID to retrieve details for")) -> dict:
        """Get detailed credit card information"""
        return await api_client.get(f"/api/credit-cards/{card_id}")

    @mcp.tool(
        name="update_credit_card",
        description="Update existing credit card information including holder name, expiry date, product type, credit limits, and activation status. Supports partial updates while maintaining security and data integrity for ongoing account management.",
        tags={"credit_cards", "card_management", "account_updates", "customer_service"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def update_credit_card(
        card_id: int = Path(..., description="Credit card ID to update"),
        card: CreditCardUpdate = Body(..., description="Updated credit card information")
    ) -> dict:
        """Update credit card information"""
        card_data = card.model_dump(exclude_unset=True)
        if card_data.get("product_type"):
            card_data["product_type"] = card_data["product_type"].value if hasattr(card_data["product_type"], "value") else card_data["product_type"]
        return await api_client.put(f"/api/credit-cards/{card_id}", data=card_data)

    @mcp.tool(
        name="delete_credit_card",
        description="Remove a credit card from the system. Permanently deletes card information and deactivates all associated payment capabilities. Use with caution as this action cannot be undone and may affect pending transactions.",
        tags={"credit_cards", "card_deletion", "account_management", "security"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def delete_credit_card(card_id: int = Path(..., description="Credit card ID to delete")) -> dict:
        """Delete a credit card"""
        return await api_client.delete(f"/api/credit-cards/{card_id}")

    @mcp.tool(
        name="activate_credit_card",
        description="Activate a credit card to enable payment processing and transaction capabilities. Sets the card status to active and allows the card to be used for purchases, payments, and reward earning activities.",
        tags={"credit_cards", "card_activation", "payment_processing", "account_management"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def activate_credit_card(card_id: int = Path(..., description="Credit card ID to activate")) -> dict:
        """Activate a credit card"""
        return await api_client.post(f"/api/credit-cards/{card_id}/activate")

    @mcp.tool(
        name="deactivate_credit_card",
        description="Deactivate a credit card to suspend payment processing and transaction capabilities. Sets the card status to inactive, preventing new transactions while preserving card data and transaction history for security and compliance.",
        tags={"credit_cards", "card_deactivation", "security", "account_management"},
        meta={"version": "1.0", "category": "credit_card_management"}
    )
    async def deactivate_credit_card(card_id: int = Path(..., description="Credit card ID to deactivate")) -> dict:
        """Deactivate a credit card"""
        return await api_client.post(f"/api/credit-cards/{card_id}/deactivate")
