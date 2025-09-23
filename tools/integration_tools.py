from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    CardToken, CardTokenRequest, TokenValidationResponse,
    HotelSearchRequest, HotelBookingRequest, FlightSearchRequest, FlightBookingRequest,
    TravelPackageSearchRequest, ShoppingProductSearch, ShoppingCartItem, ShoppingOrder,
    api_client
)

def register_integration_tools(mcp: FastMCP):
    """Register integration-related MCP tools - token management, travel, and shopping integrations"""

    # === Token Management Tools (API endpoints) ===
    @mcp.tool(
        name="create_card_token",
        description="Generate a secure tokenized representation of a credit card for safe payment processing and recurring transactions. Creates single-use, multi-use, or recurring tokens with configurable expiry times for enhanced payment security and PCI compliance.",
        tags={"security", "tokenization", "payment_processing", "pci_compliance"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def create_card_token(token_request: CardTokenRequest = Body(..., description="Token creation request with card ID, token type, and expiry configuration")) -> dict:
        """Create a secure card token - matches swagger POST /api/tokens/create"""
        token_data = token_request.model_dump(exclude_unset=True)
        return await api_client.post("/api/tokens/create", data=token_data)

    @mcp.tool(
        name="validate_card_token",
        description="Validate a card token and retrieve associated card information for payment processing. Checks token validity, expiry status, usage limits, and returns card details for secure transaction authorization without exposing sensitive card data.",
        tags={"security", "tokenization", "validation", "payment_processing"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def validate_card_token(token_id: str = Path(..., description="Card token ID to validate")) -> dict:
        """Validate a card token - matches swagger POST /api/tokens/{token_id}/validate"""
        return await api_client.post(f"/api/tokens/{token_id}/validate")

    @mcp.tool(
        name="get_token_details",
        description="Retrieve detailed information about a specific card token including creation date, expiry, usage count, and status for token management and security monitoring.",
        tags={"security", "tokenization", "token_management", "monitoring"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def get_token_details(token_id: str = Path(..., description="Card token ID to retrieve details for")) -> dict:
        """Get token details - matches swagger GET /api/tokens/{token_id}"""
        return await api_client.get(f"/api/tokens/{token_id}")

    @mcp.tool(
        name="deactivate_card_token",
        description="Deactivate an active card token to prevent further usage. Immediately invalidates the token for security purposes, useful for compromised tokens, customer requests, or expired card scenarios with full audit trail.",
        tags={"security", "tokenization", "deactivation", "access_control"},
        meta={"version": "1.0", "category": "payment_security"}
    )
    async def deactivate_card_token(token_id: str = Path(..., description="Card token ID to deactivate")) -> dict:
        """Deactivate a card token - matches swagger POST /api/tokens/{token_id}/deactivate"""
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
        """Get tokens for a specific card - matches swagger GET /api/tokens/card/{card_id}/tokens"""
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
        """Get all tokens for a customer - matches swagger GET /api/tokens/customer/{customer_id}"""
        params = {}
        if is_active is not None:
            params["is_active"] = is_active
        return await api_client.get(f"/api/tokens/customer/{customer_id}", params=params)

    # === Hotel Integration Tools (/offers/hotel/ endpoints) ===
    @mcp.tool(
        name="search_hotels",
        description="Search for available hotels based on location, dates, and occupancy requirements. Returns hotel options with pricing, amenities, availability, and booking details for travel planning and reservation services.",
        tags={"travel", "hotels", "search", "accommodations"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def search_hotels(search: HotelSearchRequest = Body(..., description="Hotel search criteria including city, dates, rooms, and guests")) -> dict:
        """Search for available hotels - matches swagger POST /offers/hotel/search-hotels"""
        search_data = search.model_dump(exclude_unset=True)
        return await api_client.post("/offers/hotel/search-hotels", data=search_data)

    @mcp.tool(
        name="book_hotel",
        description="Create a hotel booking with guest information, room requirements, and payment details. Processes reservation confirmation, handles payment authorization, and provides booking confirmation with full itinerary details.",
        tags={"travel", "hotels", "booking", "reservations"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def book_hotel(booking: HotelBookingRequest = Body(..., description="Hotel booking details including hotel, customer, dates, and guest information")) -> dict:
        """Book a hotel - matches swagger POST /offers/hotel/book-hotel"""
        booking_data = booking.model_dump(exclude_unset=True)
        return await api_client.post("/offers/hotel/book-hotel", data=booking_data)

    @mcp.tool(
        name="get_hotel_booking_details",
        description="Retrieve detailed information about a specific hotel booking including confirmation details, guest information, and booking status for customer service and travel management.",
        tags={"travel", "hotels", "booking_details", "customer_service"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def get_hotel_booking_details(booking_reference: str = Path(..., description="Hotel booking reference")) -> dict:
        """Get hotel booking details - matches swagger GET /offers/hotel/booking/{booking_reference}"""
        return await api_client.get(f"/offers/hotel/booking/{booking_reference}")

    @mcp.tool(
        name="get_available_cities",
        description="Retrieve list of available cities for hotel bookings. Provides destination options for travel planning and hotel search functionality with city-specific information.",
        tags={"travel", "hotels", "cities", "destinations"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def get_available_cities() -> dict:
        """Get available cities for hotel bookings - matches swagger GET /offers/hotel/cities"""
        return await api_client.get("/offers/hotel/cities")

    # === Flight Integration Tools (/offers/travel/ endpoints) ===
    @mcp.tool(
        name="search_flights",
        description="Search for available flights based on origin, destination, dates, and passenger count. Returns flight options with schedules, pricing, airlines, and booking availability for travel planning and flight reservations.",
        tags={"travel", "flights", "search", "airlines"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def search_flights(search: FlightSearchRequest = Body(..., description="Flight search criteria including origin, destination, dates, and passengers")) -> dict:
        """Search for available flights - matches swagger POST /offers/travel/search-flights"""
        search_data = search.model_dump(exclude_unset=True)
        return await api_client.post("/offers/travel/search-flights", data=search_data)

    @mcp.tool(
        name="book_flight",
        description="Create a flight booking with passenger information and payment details. Processes seat reservations, handles payment authorization, and provides booking confirmation with e-tickets and itinerary information.",
        tags={"travel", "flights", "booking", "airlines"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def book_flight(booking: FlightBookingRequest = Body(..., description="Flight booking details including flight, customer, and passenger information")) -> dict:
        """Book a flight - matches swagger POST /offers/travel/book-flight"""
        booking_data = booking.model_dump(exclude_unset=True)
        return await api_client.post("/offers/travel/book-flight", data=booking_data)

    @mcp.tool(
        name="get_flight_booking_details",
        description="Retrieve detailed information about a specific flight booking including ticket details, passenger information, and flight status for customer service and travel management.",
        tags={"travel", "flights", "booking_details", "customer_service"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def get_flight_booking_details(booking_reference: str = Path(..., description="Flight booking reference")) -> dict:
        """Get flight booking details - matches swagger GET /offers/travel/booking/{booking_reference}"""
        return await api_client.get(f"/offers/travel/booking/{booking_reference}")

    @mcp.tool(
        name="get_available_airports",
        description="Retrieve list of available airports for flight bookings. Provides airport codes and information for flight search functionality and travel planning with comprehensive airport data.",
        tags={"travel", "flights", "airports", "destinations"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def get_available_airports() -> dict:
        """Get available airports for flight bookings - matches swagger GET /offers/travel/airports"""
        return await api_client.get("/offers/travel/airports")

    @mcp.tool(
        name="search_travel_packages",
        description="Search for comprehensive travel packages including flights, hotels, and activities based on destination, dates, and traveler requirements. Returns package options with bundled pricing and complete itinerary details.",
        tags={"travel", "packages", "search", "vacation_planning"},
        meta={"version": "1.0", "category": "travel_services"}
    )
    async def search_travel_packages(search: TravelPackageSearchRequest = Body(..., description="Travel package search criteria including destinations, dates, and traveler preferences")) -> dict:
        """Search for travel packages - matches swagger POST /offers/search/travel-package"""
        search_data = search.model_dump(exclude_unset=True)
        return await api_client.post("/offers/search/travel-package", data=search_data)

    # === Shopping Integration Tools (/offers/shopping/ endpoints) ===
    @mcp.tool(
        name="search_shopping_products",
        description="Search the integrated shopping catalog for products based on query, category, brand, and price filters. Returns product listings with descriptions, pricing, availability, and purchase options for e-commerce integration and customer shopping.",
        tags={"shopping", "e-commerce", "product_search", "catalog"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def search_shopping_products(search: ShoppingProductSearch = Body(..., description="Product search criteria including query, category, brand, and price filters")) -> dict:
        """Search shopping products - matches swagger POST /offers/shopping/search"""
        search_data = search.model_dump(exclude_unset=True)
        return await api_client.post("/offers/shopping/search", data=search_data)

    @mcp.tool(
        name="get_product_details",
        description="Retrieve detailed information about a specific product including description, pricing, availability, specifications, and customer reviews for comprehensive product information and purchase decision support.",
        tags={"shopping", "product_details", "e-commerce", "product_information"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def get_product_details(product_id: str = Path(..., description="Product ID to retrieve details for")) -> dict:
        """Get detailed product information - matches swagger GET /offers/shopping/product/{product_id}"""
        return await api_client.get(f"/offers/shopping/product/{product_id}")

    @mcp.tool(
        name="get_shopping_categories",
        description="Retrieve all available shopping categories for product filtering and navigation. Provides organized category structure for enhanced shopping experience and product discovery.",
        tags={"shopping", "categories", "navigation", "product_discovery"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def get_shopping_categories() -> dict:
        """Get available shopping categories - matches swagger GET /offers/shopping/categories"""
        return await api_client.get("/offers/shopping/categories")

    @mcp.tool(
        name="get_shopping_brands",
        description="Retrieve all available brands for product filtering and brand-specific shopping. Provides comprehensive brand listings for targeted product searches and brand loyalty programs.",
        tags={"shopping", "brands", "filtering", "brand_loyalty"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def get_shopping_brands() -> dict:
        """Get available shopping brands - matches swagger GET /offers/shopping/brands"""
        return await api_client.get("/offers/shopping/brands")

    @mcp.tool(
        name="add_to_shopping_cart",
        description="Add a product to customer's shopping cart with specified quantity. Manages cart state, inventory checking, pricing calculations, and prepares items for checkout with automatic cart optimization and recommendations.",
        tags={"shopping", "cart_management", "e-commerce", "customer_experience"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def add_to_shopping_cart(cart_item: ShoppingCartItem = Body(..., description="Cart item details with customer ID, product ID, and quantity")) -> dict:
        """Add item to shopping cart - matches swagger POST /offers/shopping/add-to-cart"""
        item_data = cart_item.model_dump(exclude_unset=True)
        return await api_client.post("/offers/shopping/add-to-cart", data=item_data)

    @mcp.tool(
        name="create_shopping_order",
        description="Create a shopping order from cart contents with shipping and payment information. Processes inventory allocation, payment authorization, shipping arrangements, and order confirmation with tracking details and delivery estimates.",
        tags={"shopping", "order_processing", "checkout", "fulfillment"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def create_shopping_order(order: ShoppingOrder = Body(..., description="Shopping order details with customer ID, shipping address, and payment method")) -> dict:
        """Create shopping order - matches swagger POST /offers/shopping/create-order"""
        order_data = order.model_dump(exclude_unset=True)
        return await api_client.post("/offers/shopping/create-order", data=order_data)

    @mcp.tool(
        name="get_shopping_order_details",
        description="Retrieve detailed information about a specific shopping order including items, pricing, shipping status, and delivery tracking for comprehensive order management and customer service.",
        tags={"shopping", "order_details", "tracking", "customer_service"},
        meta={"version": "1.0", "category": "shopping_integration"}
    )
    async def get_shopping_order_details(order_id: str = Path(..., description="Shopping order ID to retrieve details for")) -> dict:
        """Get shopping order details - matches swagger GET /offers/shopping/order/{order_id}"""
        return await api_client.get(f"/offers/shopping/order/{order_id}")

    # === System Status Tool ===
    @mcp.tool(
        name="check_integration_status",
        description="Check the operational status of all integrated services including payment processors, travel booking systems, shopping platforms, and external APIs. Returns real-time status information for system monitoring and troubleshooting.",
        tags={"monitoring", "system_status", "integrations", "diagnostics"},
        meta={"version": "1.0", "category": "system_monitoring"}
    )
    async def check_integration_status() -> dict:
        """Check status of all integrated services - matches swagger GET /simulator/status"""
        return await api_client.get("/simulator/status")
