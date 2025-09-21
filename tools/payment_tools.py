from fastmcp import FastMCP
from fastapi import Query, Body
from typing import Optional
from datetime import datetime
from models import (
    Payment, PaymentCreate, PaymentListResponse, PaymentResponse, PaymentStatus
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
        customer_id: Optional[int] = Query(None, description="Filter payments by specific customer ID"),
        start_date: Optional[str] = Query(None, description="Filter payments from this date (YYYY-MM-DD format)"),
        end_date: Optional[str] = Query(None, description="Filter payments until this date (YYYY-MM-DD format)"),
        status: Optional[PaymentStatus] = Query(None, description="Filter by payment status (PENDING, COMPLETED, FAILED, REFUNDED)")
    ) -> PaymentListResponse:
        """List payments with various filtering options"""
        # Stub implementation - replace with actual database logic
        return PaymentListResponse(payments=[], total=0)

    @mcp.tool(
        name="make_payment",
        description="Process a new credit card payment transaction with automatic rewards calculation and offer application. Handles payment validation, merchant verification, real-time transaction processing, and generates rewards points based on spending patterns.",
        tags={"payments", "transaction_processing", "rewards", "offers", "credit_cards"},
        meta={"version": "1.0", "category": "payment_processing"}
    )
    async def make_payment(payment: PaymentCreate = Body(..., description="Payment details including credit card, amount, merchant, and transaction information")) -> PaymentResponse:
        """Process a new payment transaction"""
        # Stub implementation - replace with actual payment processing logic
        new_payment = Payment(
            id=1,
            credit_card_id=payment.credit_card_id,
            amount=payment.amount,
            merchant_name=payment.merchant_name,
            merchant_category=payment.merchant_category,
            status=PaymentStatus.COMPLETED,
            transaction_date=datetime.utcnow(),
            description=payment.description
        )

        return PaymentResponse(
            payment=new_payment,
            rewards_earned=int(payment.amount),  # 1 point per dollar
            offers_applied=[]
        )
