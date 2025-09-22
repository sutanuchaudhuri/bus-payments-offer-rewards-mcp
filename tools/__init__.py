from .health_tools import register_health_tools
from .customer_tools import register_customer_tools
from .credit_card_tools import register_credit_card_tools
from .merchant_tools import register_merchant_tools
from .payment_tools import register_payment_tools
from .offer_tools import register_offer_tools
from .reward_tools import register_reward_tools
from .profile_history_tools import register_profile_history_tools
from .refund_tools import register_refund_tools
from .booking_tools import register_booking_tools
from .integration_tools import register_integration_tools

def register_all_tools(mcp):
    """Register all MCP tools with the FastMCP instance"""
    register_health_tools(mcp)
    register_customer_tools(mcp)
    register_credit_card_tools(mcp)
    register_merchant_tools(mcp)
    register_payment_tools(mcp)
    register_offer_tools(mcp)
    register_reward_tools(mcp)
    register_profile_history_tools(mcp)
    register_refund_tools(mcp)
    register_booking_tools(mcp)
    register_integration_tools(mcp)

__all__ = [
    "register_health_tools",
    "register_customer_tools",
    "register_credit_card_tools",
    "register_merchant_tools",
    "register_payment_tools",
    "register_offer_tools",
    "register_reward_tools",
    "register_profile_history_tools",
    "register_refund_tools",
    "register_booking_tools",
    "register_integration_tools",
    "register_all_tools"
]
