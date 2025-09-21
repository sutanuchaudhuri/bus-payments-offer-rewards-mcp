from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from datetime import datetime
from models import (
    Customer, CustomerCreate, CustomerUpdate, CustomerListResponse
)

def register_customer_tools(mcp: FastMCP):
    """Register customer-related MCP tools"""

    @mcp.tool(
        name="list_customers",
        description="Retrieve a paginated list of all customers in the system with optional email filtering. Returns customer profiles including personal information, contact details, and account creation timestamps.",
        tags={"customers", "user_management", "profiles"},
        meta={"version": "1.0", "category": "customer_management"}
    )
    async def list_customers(
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of customers per page"),
        email: Optional[str] = Query(None, description="Filter customers by email address")
    ) -> CustomerListResponse:
        """List all customers with pagination and optional email filtering"""
        # Stub implementation - replace with actual database logic
        return CustomerListResponse(
            customers=[],
            total=0,
            page=page,
            per_page=per_page,
            pages=0
        )

    @mcp.tool(
        name="create_customer",
        description="Register a new customer account with personal information including name, email, phone, date of birth, and address. Creates a unique customer profile for credit card and payment management.",
        tags={"customers", "registration", "account_creation"},
        meta={"version": "1.0", "category": "customer_management"}
    )
    async def create_customer(customer: CustomerCreate = Body(...)) -> Customer:
        """Create a new customer account"""
        # Stub implementation - replace with actual database logic
        return Customer(
            id=1,
            **customer.dict(),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

    @mcp.tool(
        name="get_customer_details",
        description="Retrieve detailed information about a specific customer including full profile, contact information, registration date, and account status. Used for customer service and account management.",
        tags={"customers", "profile", "account_details"},
        meta={"version": "1.0", "category": "customer_management"}
    )
    async def get_customer_details(customer_id: int = Path(..., description="Unique customer identifier")) -> Customer:
        """Get detailed information about a specific customer"""
        # Stub implementation - replace with actual database logic
        return Customer(
            id=customer_id,
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="+1234567890",
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )

    @mcp.tool(
        name="update_customer",
        description="Update existing customer information including personal details, contact information, and address. Supports partial updates and maintains data integrity for customer profiles.",
        tags={"customers", "profile_update", "account_management"},
        meta={"version": "1.0", "category": "customer_management"}
    )
    async def update_customer(
        customer_id: int = Path(..., description="Unique customer identifier"),
        customer: CustomerUpdate = Body(...)
    ) -> dict:
        """Update customer information"""
        # Stub implementation - replace with actual database logic
        return {"message": "Customer updated successfully"}

    @mcp.tool(
        name="delete_customer",
        description="Permanently remove a customer account and all associated data from the system. This action is irreversible and will also remove linked credit cards, payment history, and rewards.",
        tags={"customers", "account_deletion", "data_management"},
        meta={"version": "1.0", "category": "customer_management"}
    )
    async def delete_customer(customer_id: int = Path(..., description="Unique customer identifier")) -> dict:
        """Delete a customer account"""
        # Stub implementation - replace with actual database logic
        return {"message": "Customer deleted successfully"}
