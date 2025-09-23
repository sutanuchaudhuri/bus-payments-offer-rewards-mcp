from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
import os
from models import (
    Customer, CustomerCreate, CustomerUpdate, CustomerListResponse, api_client
)

def register_customer_tools(mcp: FastMCP):
    """Register customer-related MCP tools"""

    # Read customer admin tools enabled setting from environment
    customer_admin_enabled = os.getenv("CUSTOMER_ADMIN_ENABLED", "false").lower() == "true"

    @mcp.tool(
        name="list_customers",
        description="Retrieve a paginated list of all customers in the system with optional email filtering. Returns customer profiles including personal information, contact details, and account creation timestamps for customer management and analytics.",
        tags={"customers", "user_management", "profiles", "search"},
        meta={"version": "1.0", "category": "customer_management"},
        enabled=customer_admin_enabled
    )
    async def list_customers(
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of customers per page"),
        email: Optional[str] = Query(None, description="Filter customers by email address")
    ) -> dict:
        """List all customers with pagination and optional email filtering"""
        params = {"page": page, "per_page": per_page}
        if email:
            params["email"] = email
        return await api_client.get("/api/customers", params=params)

    @mcp.tool(
        name="create_customer",
        description="Register a new customer account with personal information including name, email, phone, date of birth, and address. Creates a unique customer profile for credit card and payment management with full data validation and duplicate email prevention.",
        tags={"customers", "registration", "account_creation", "onboarding"},
        meta={"version": "1.0", "category": "customer_management"},
        enabled=customer_admin_enabled
    )
    async def create_customer(customer: CustomerCreate = Body(..., description="Customer registration details including required name and email, plus optional contact and personal information")) -> dict:
        """Create a new customer account"""
        customer_data = customer.model_dump(exclude_unset=True)
        return await api_client.post("/api/customers", data=customer_data)

    @mcp.tool(
        name="get_customer_details",
        description="Retrieve detailed information about a specific customer including full profile, contact information, registration date, and account status. Used for customer service, account management, and support operations.",
        tags={"customers", "details", "profile", "support"},
        meta={"version": "1.0", "category": "customer_management"}
    )
    async def get_customer_details(customer_id: str = Path(..., description="Customer alphanumeric ID to retrieve")) -> dict:
        """Get detailed customer information"""
        return await api_client.get(f"/api/customers/{customer_id}")

    @mcp.tool(
        name="update_customer",
        description="Update existing customer information including name, email, phone, address, and personal details. Supports partial updates and maintains data integrity with email uniqueness validation.",
        tags={"customers", "update", "profile_management", "data_maintenance"},
        meta={"version": "1.0", "category": "customer_management"},
        enabled=customer_admin_enabled
    )
    async def update_customer(
        customer_id: str = Path(..., description="Customer alphanumeric ID to update"),
        customer: CustomerUpdate = Body(..., description="Updated customer information")
    ) -> dict:
        """Update customer information"""
        customer_data = customer.model_dump(exclude_unset=True)
        return await api_client.put(f"/api/customers/{customer_id}", data=customer_data)

    @mcp.tool(
        name="delete_customer",
        description="Remove a customer account from the system. Permanently deletes customer profile and associated data. Use with caution as this action cannot be undone and may affect related transactions and credit cards.",
        tags={"customers", "deletion", "account_removal", "data_cleanup"},
        meta={"version": "1.0", "category": "customer_management"},
        enabled=customer_admin_enabled
    )
    async def delete_customer(customer_id: str = Path(..., description="Customer alphanumeric ID to delete")) -> dict:
        """Delete a customer account"""
        return await api_client.delete(f"/api/customers/{customer_id}")
