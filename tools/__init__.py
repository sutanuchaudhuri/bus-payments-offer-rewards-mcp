from .health_tools import register_health_tools
from .customer_tools import register_customer_tools
from .credit_card_tools import register_credit_card_tools
from .merchant_tools import register_merchant_tools
from .payment_tools import register_payment_tools
from .offer_tools import register_offer_tools
from .reward_tools import register_reward_tools
from .refund_tools import register_refund_tools
from .booking_tools import register_booking_tools
from .integration_tools import register_integration_tools

def register_all_tools(mcp):
    """Register all MCP tools with the FastMCP instance - cleaned up to match swagger.json exactly"""
    register_health_tools(mcp)           # 1 tool: /api/health
    register_customer_tools(mcp)         # 5 tools: /api/customers/*
    register_credit_card_tools(mcp)      # 4 tools: /api/customers/{id}/credit-cards/*
    register_merchant_tools(mcp)         # 7 tools: /api/merchants/*
    register_payment_tools(mcp)          # 5 tools: /api/payments/*
    register_offer_tools(mcp)            # 9 tools: /api/offers/*
    register_reward_tools(mcp)           # 8 tools: /api/rewards/*
    register_refund_tools(mcp)           # 6 tools: /api/refunds/*
    register_booking_tools(mcp)          # 2 tools: /api/bookings/* (minimal API)
    register_integration_tools(mcp)      # 24 tools: /api/tokens/*, /offers/*, /simulator/*
    # Total: 71 tools matching swagger.json exactly

__all__ = [
    "register_health_tools",
    "register_customer_tools",
    "register_credit_card_tools",
    "register_merchant_tools",
    "register_payment_tools",
    "register_offer_tools",
    "register_reward_tools",
    "register_refund_tools",
    "register_booking_tools",
    "register_integration_tools",
    "register_all_tools"
]
