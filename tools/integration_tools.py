from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    CardToken, CardTokenRequest, TokenValidationResponse, ShoppingProductSearch,
    ShoppingCartItem, ShoppingOrder, IntegrationStatus, TokenType, api_client
)

def register_integration_tools(mcp: FastMCP):
    """Register integration-related MCP tools"""

    @mcp.tool(
        name="create_card_token",
        description="Generate a secure tokenized representation of a credit card for safe payment processing and recurring transactions. Creates single-use, multi-use, or recurring tokens with configurable expiry times for enhanced payment security and PCI compliance.",
        tags={"security", "tokenization", "payment_processing", "pci_compliance"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def create_card_token(token_request: CardTokenRequest = Body(..., description="Token creation request with card ID, token type, and expiry configuration")) -> dict:
        """Create a secure card token"""
        token_data = token_request.model_dump(exclude_unset=True)
        if token_data.get("token_type"):
            token_data["token_type"] = token_data["token_type"].value if hasattr(token_data["token_type"], "value") else token_data["token_type"]
        return await api_client.post("/api/tokens/create", data=token_data)

    @mcp.tool(
        name="validate_card_token",
        description="Validate a card token and retrieve associated card information for payment processing. Checks token validity, expiry status, usage limits, and returns card details for secure transaction authorization without exposing sensitive card data.",
        tags={"security", "tokenization", "validation", "payment_processing"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def validate_card_token(token_id: str = Path(..., description="Card token ID to validate")) -> dict:
        """Validate a card token"""
        return await api_client.post(f"/api/tokens/{token_id}/validate")

    @mcp.tool(
        name="get_token_details",
        description="Retrieve detailed information about a specific card token including creation date, expiry, usage count, and status for token management and security monitoring.",
        tags={"security", "tokenization", "token_management", "monitoring"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def get_token_details(token_id: str = Path(..., description="Card token ID to retrieve details for")) -> dict:
        """Get token details"""
        return await api_client.get(f"/api/tokens/{token_id}")

    @mcp.tool(
        name="deactivate_card_token",
        description="Deactivate an active card token to prevent further usage. Immediately invalidates the token for security purposes, useful for compromised tokens, customer requests, or expired card scenarios with full audit trail.",
        tags={"security", "tokenization", "deactivation", "access_control"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def deactivate_card_token(token_id: str = Path(..., description="Card token ID to deactivate")) -> dict:
        """Deactivate a card token"""
        return await api_client.post(f"/api/tokens/{token_id}/deactivate")

    @mcp.tool(
        name="get_card_tokens",
        description="Retrieve all tokens associated with a specific credit card including active and inactive tokens for comprehensive token management and security oversight.",
        tags={"security", "tokenization", "card_management", "monitoring"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def get_card_tokens(
        card_id: int = Path(..., description="Credit card ID to retrieve tokens for"),
        is_active: Optional[bool] = Query(None, description="Filter by token active status")
    ) -> dict:
        """Get tokens for a specific card"""
        params = {}
        if is_active is not None:
            params["is_active"] = is_active
        return await api_client.get(f"/api/tokens/card/{card_id}/tokens", params=params)

    @mcp.tool(
        name="get_customer_tokens",
        description="Retrieve all tokens associated with a specific customer across all their credit cards for comprehensive customer token management and security monitoring.",
        tags={"security", "tokenization", "customer_management", "monitoring"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def get_customer_tokens(
        customer_id: int = Path(..., description="Customer ID to retrieve tokens for"),
        is_active: Optional[bool] = Query(None, description="Filter by token active status")
    ) -> dict:
        """Get all tokens for a customer"""
        params = {}
        if is_active is not None:
            params["is_active"] = is_active
        return await api_client.get(f"/api/tokens/customer/{customer_id}", params=params)

    @mcp.tool(
        name="search_shopping_products",
        description="Search the integrated shopping catalog for products based on query, category, brand, and price filters. Returns product listings with descriptions, pricing, availability, and purchase options for e-commerce integration and customer shopping.",
        tags={"shopping", "e-commerce", "product_search", "catalog"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def search_shopping_products(search: ShoppingProductSearch = Body(..., description="Product search criteria including query, category, brand, and price filters")) -> dict:
        """Search shopping products"""
        search_data = search.model_dump(exclude_unset=True)
        return await api_client.post("/offers/shopping/search", data=search_data)

    @mcp.tool(
        name="get_product_details",
        description="Retrieve detailed information about a specific product including description, pricing, availability, specifications, and customer reviews for comprehensive product information and purchase decision support.",
        tags={"shopping", "product_details", "e-commerce", "product_information"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def get_product_details(product_id: str = Path(..., description="Product ID to retrieve details for")) -> dict:
        """Get detailed product information"""
        return await api_client.get(f"/offers/shopping/product/{product_id}")

    @mcp.tool(
        name="get_shopping_categories",
        description="Retrieve all available shopping categories for product filtering and navigation. Provides organized category structure for enhanced shopping experience and product discovery.",
        tags={"shopping", "categories", "navigation", "product_discovery"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def get_shopping_categories() -> dict:
        """Get available shopping categories"""
        return await api_client.get("/offers/shopping/categories")

    @mcp.tool(
        name="get_shopping_brands",
        description="Retrieve all available brands for product filtering and brand-specific shopping. Provides comprehensive brand listings for targeted product searches and brand loyalty programs.",
        tags={"shopping", "brands", "filtering", "brand_loyalty"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def get_shopping_brands() -> dict:
        """Get available shopping brands"""
        return await api_client.get("/offers/shopping/brands")

    @mcp.tool(
        name="add_to_shopping_cart",
        description="Add a product to customer's shopping cart with specified quantity. Manages cart state, inventory checking, pricing calculations, and prepares items for checkout with automatic cart optimization and recommendations.",
        tags={"shopping", "cart_management", "e-commerce", "customer_experience"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def add_to_shopping_cart(cart_item: ShoppingCartItem = Body(..., description="Cart item details with customer ID, product ID, and quantity")) -> dict:
        """Add item to shopping cart"""
        item_data = cart_item.model_dump(exclude_unset=True)
        return await api_client.post("/offers/shopping/add-to-cart", data=item_data)

    @mcp.tool(
        name="create_shopping_order",
        description="Create a shopping order from cart contents with shipping and payment information. Processes inventory allocation, payment authorization, shipping arrangements, and order confirmation with tracking details and delivery estimates.",
        tags={"shopping", "order_processing", "checkout", "fulfillment"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def create_shopping_order(order: ShoppingOrder = Body(..., description="Shopping order details with customer ID, shipping address, and payment method")) -> dict:
        """Create shopping order"""
        order_data = order.model_dump(exclude_unset=True)
        return await api_client.post("/offers/shopping/create-order", data=order_data)

    @mcp.tool(
        name="get_shopping_order_details",
        description="Retrieve detailed information about a specific shopping order including items, pricing, shipping status, and delivery tracking for comprehensive order management and customer service.",
        tags={"shopping", "order_details", "tracking", "customer_service"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def get_shopping_order_details(order_id: str = Path(..., description="Shopping order ID to retrieve details for")) -> dict:
        """Get shopping order details"""
        return await api_client.get(f"/offers/shopping/order/{order_id}")

    @mcp.tool(
        name="check_integration_status",
        description="Check the operational status of all integrated services including payment processors, travel booking systems, shopping platforms, and external APIs. Returns real-time status information for system monitoring and troubleshooting.",
        tags={"monitoring", "system_status", "integrations", "diagnostics"},
        meta={"version": "1.0", "category": "system_monitoring"}
    )
    async def check_integration_status() -> dict:
        """Check status of all integrated services"""
        return await api_client.get("/simulator/status")
