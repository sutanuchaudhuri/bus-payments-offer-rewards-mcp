from fastmcp import FastMCP
from fastapi import Query, Path, Body
from typing import Optional
from models import (
    Payment, PaymentCreate, PaymentRefund, PaymentListResponse,
    PaymentStatus, SpendingAnalytics, api_client
)

def register_payment_tools(mcp: FastMCP):
    """Register payment-related MCP tools"""

    @mcp.tool(
        name="list_payments",
        description="Retrieve a comprehensive list of payment transactions with advanced filtering options by customer, date range, and payment status. Returns detailed payment history including amounts, merchants, transaction dates, and status tracking for financial reporting and analysis.",
        tags={"payments", "transactions", "financial_history", "reporting"},
        meta={"version": "1.0", "category": "payment_processing"}
    )
    async def list_payments(
        page: int = Query(1, description="Page number for pagination"),
        per_page: int = Query(10, description="Number of payments per page"),
        customer_id: Optional[int] = Query(None, description="Filter payments by specific customer ID"),
        start_date: Optional[str] = Query(None, description="Filter payments from this date (YYYY-MM-DD format)"),
        end_date: Optional[str] = Query(None, description="Filter payments until this date (YYYY-MM-DD format)"),
        status: Optional[PaymentStatus] = Query(None, description="Filter by payment status (PENDING, COMPLETED, FAILED, REFUNDED)")
    ) -> dict:
        """List payments with various filtering options"""
        params = {"page": page, "per_page": per_page}
        if customer_id:
            params["customer_id"] = customer_id
        if start_date:
            params["start_date"] = start_date
        if end_date:
            params["end_date"] = end_date
        if status:
            # Convert enum to string for API compatibility
            params["status"] = status.value if hasattr(status, 'value') else str(status)
        return await api_client.get("/api/payments", params=params)

    @mcp.tool(
        name="make_payment",
        description="Process a new credit card payment transaction with automatic rewards calculation and offer application. Handles payment validation, merchant verification, real-time transaction processing, and generates rewards points based on spending patterns and activated offers.",
        tags={"payments", "transaction_processing", "rewards", "offers", "credit_cards"},
        meta={"version": "1.0", "category": "payment_processing"}
    )
    async def make_payment(payment: PaymentCreate = Body(..., description="Payment details including credit card, amount, merchant, and transaction information")) -> dict:
        """Process a new payment transaction"""
        payment_data = payment.model_dump(exclude_unset=True)
        return await api_client.post("/api/payments", data=payment_data)

    @mcp.tool(
        name="get_payment_details",
        description="Retrieve detailed information about a specific payment transaction including amount, merchant details, status, timestamp, associated rewards earned, and any applied offers for comprehensive transaction tracking and customer service.",
        tags={"payments", "transaction_details", "customer_service", "tracking"},
        meta={"version": "1.0", "category": "payment_processing"}
    )
    async def get_payment_details(payment_id: int = Path(..., description="Payment ID to retrieve details for")) -> dict:
        """Get detailed payment information"""
        return await api_client.get(f"/api/payments/{payment_id}")

    @mcp.tool(
        name="refund_payment",
        description="Process a full or partial refund for a completed payment transaction. Handles refund validation, amount verification, and automatic adjustment of rewards points and offer benefits based on the refunded amount.",
        tags={"payments", "refunds", "transaction_reversal", "customer_service"},
        meta={"version": "1.0", "category": "payment_processing"}
    )
    async def refund_payment(
        payment_id: int = Path(..., description="Payment ID to refund"),
        refund: PaymentRefund = Body(..., description="Refund details including optional partial amount")
    ) -> dict:
        """Process a payment refund"""
        refund_data = refund.model_dump(exclude_unset=True)
        return await api_client.post(f"/api/payments/{payment_id}/refund", data=refund_data)

    @mcp.tool(
        name="get_spending_analytics",
        description="Retrieve comprehensive spending analytics for a customer including total amounts, transaction counts, category breakdowns, merchant analysis, and spending patterns over specified time periods for financial insights and budgeting assistance.",
        tags={"payments", "analytics", "spending_analysis", "financial_insights", "reporting"},
        meta={"version": "1.0", "category": "payment_processing"}
    )
    async def get_spending_analytics(
        customer_id: int = Path(..., description="Customer ID for spending analytics"),
        period: Optional[str] = Query("month", description="Analytics period (day, week, month, year)")
    ) -> dict:
        """Get customer spending analytics"""
        params = {"period": period}
        return await api_client.get(f"/api/customers/{customer_id}/spending-analytics", params=params)
