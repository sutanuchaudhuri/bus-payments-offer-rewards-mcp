from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    Refund, RefundRequest, PointsRefundRequest, RefundApproval, RefundDenial,
    RefundListResponse, RefundStatus, RefundType, api_client
)

def register_refund_tools(mcp: FastMCP):
    """Register refund-related MCP tools"""

    @mcp.tool(
        name="list_refunds",
        description="Retrieve a comprehensive list of all refund requests in the system with filtering by customer, status, and type. Returns detailed refund information including amounts, reasons, status, processing dates, and admin notes for refund management and analytics.",
        tags={"refunds", "customer_service", "disputes", "financial_operations"},
        meta={"version": "1.0", "category": "refund_management"}
    )
    async def list_refunds(
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of refunds per page"),
        customer_id: Optional[str] = Query(None, description="Filter refunds by specific customer alphanumeric ID"),
        status: Optional[RefundStatus] = Query(None, description="Filter by refund status"),
        refund_type: Optional[RefundType] = Query(None, description="Filter by refund type")
    ) -> dict:
        """List all refunds with filtering options"""
        params = {"page": page, "per_page": per_page}
        if customer_id:
            params["customer_id"] = customer_id
        if status:
            params["status"] = status.value if hasattr(status, 'value') else str(status)
        if refund_type:
            params["refund_type"] = refund_type.value if hasattr(refund_type, 'value') else str(refund_type)
        return await api_client.get("/api/refunds", params=params)

    @mcp.tool(
        name="submit_refund_request",
        description="Submit a new refund request for a booking cancellation, dispute resolution, or goodwill gesture. Validates request details, calculates refund amounts, and initiates the approval workflow with full audit trail and customer notification.",
        tags={"refunds", "customer_service", "request_submission", "disputes"},
        meta={"version": "1.0", "category": "refund_management"}
    )
    async def submit_refund_request(refund: RefundRequest = Body(..., description="Refund request details including type, amount, reason, and related transaction information")) -> dict:
        """Submit a new refund request"""
        refund_data = refund.model_dump(exclude_unset=True)
        return await api_client.post("/api/refunds/request", data=refund_data)

    @mcp.tool(
        name="get_refund_details",
        description="Retrieve detailed information about a specific refund request including status, amounts, processing history, admin notes, approval/denial reasons, and related transaction data for comprehensive refund tracking and customer service.",
        tags={"refunds", "details", "tracking", "customer_service"},
        meta={"version": "1.0", "category": "refund_management"}
    )
    async def get_refund_details(refund_id: int = Path(..., description="Refund ID to retrieve details for")) -> dict:
        """Get detailed refund information"""
        return await api_client.get(f"/api/refunds/{refund_id}")

    @mcp.tool(
        name="approve_refund",
        description="Approve a pending refund request with optional admin notes. Processes the refund amount, updates customer balances, adjusts related rewards points, and sends confirmation notifications for complete refund resolution.",
        tags={"refunds", "approval", "administration", "financial_operations"},
        meta={"version": "1.0", "category": "refund_management"}
    )
    async def approve_refund(
        refund_id: int = Path(..., description="Refund ID to approve"),
        approval: RefundApproval = Body(..., description="Approval details with optional admin notes")
    ) -> dict:
        """Approve a refund request"""
        approval_data = approval.model_dump(exclude_unset=True)
        return await api_client.post(f"/api/refunds/{refund_id}/approve", data=approval_data)

    @mcp.tool(
        name="deny_refund",
        description="Deny a pending refund request with required denial reason and optional admin notes. Updates refund status, logs denial details, and sends notification to customer with explanation for transparency and customer service.",
        tags={"refunds", "denial", "administration", "customer_service"},
        meta={"version": "1.0", "category": "refund_management"}
    )
    async def deny_refund(
        refund_id: int = Path(..., description="Refund ID to deny"),
        denial: RefundDenial = Body(..., description="Denial details with reason")
    ) -> dict:
        """Deny a refund request"""
        denial_data = denial.model_dump(exclude_unset=True)
        return await api_client.post(f"/api/refunds/{refund_id}/deny", data=denial_data)

    @mcp.tool(
        name="request_points_refund",
        description="Submit a request to cancel points redemption and refund points to customer account. Validates redemption eligibility, calculates point restoration amounts, and processes the reversal with full transaction history and customer notification.",
        tags={"refunds", "points", "redemption_cancellation", "loyalty_program"},
        meta={"version": "1.0", "category": "refund_management"}
    )
    async def request_points_refund(points_refund: PointsRefundRequest = Body(..., description="Points refund request with customer ID, points amount, and reason")) -> dict:
        """Request a points redemption cancellation/refund"""
        refund_data = points_refund.model_dump(exclude_unset=True)
        return await api_client.post("/api/refunds/points/cancel", data=refund_data)
