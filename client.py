import asyncio
from fastmcp import Client
from models import CustomerCreate, PaymentCreate, OfferCreate
from datetime import datetime

async def test_tools():
    """Test various MCP tools with proper Pydantic model usage"""

    # Create client connection to the FastMCP server
    # The transport can be a string command to start the server process
    async with Client("stdio://python main.py") as client:
        print("🔌 Connected to ChasePaymentsRewardsOffers MCP Server")

        # List all available tools
        print("\n📋 Listing all available tools:")
        tools = await client.list_tools()
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")

        print(f"\n✅ Total tools available: {len(tools)}")

        # Test health check
        print("\n🏥 Testing health check:")
        health_result = await client.call_tool("health_check")
        print(f"Health status: {health_result.content}")

        # Test customer creation with Pydantic model
        print("\n👤 Testing customer creation with Pydantic model:")
        customer_data = CustomerCreate(
            first_name="John",
            last_name="Doe",
            email="john.doe@example.com",
            phone="+1-555-0123",
            address="123 Main St, New York, NY 10001"
        )

        customer_result = await client.call_tool("create_customer", customer=customer_data.model_dump())
        print(f"Customer created: {customer_result.content}")

        # Test listing customers
        print("\n📝 Testing customer listing:")
        customers_result = await client.call_tool("list_customers", page=1, per_page=5)
        print(f"Customers list: {customers_result.content}")

        # Test payment processing with Pydantic model
        print("\n💳 Testing payment processing:")
        payment_data = PaymentCreate(
            credit_card_id=1,
            amount=99.99,
            merchant_name="Amazon",
            merchant_category="E_COMMERCE",
            description="Online purchase"
        )

        payment_result = await client.call_tool("make_payment", payment=payment_data.model_dump())
        print(f"Payment processed: {payment_result.content}")

        # Test offer creation with Pydantic model
        print("\n🎯 Testing offer creation:")
        offer_data = OfferCreate(
            title="Holiday Special",
            description="20% off all purchases",
            category="RETAIL",
            discount_percentage=20.0,
            max_discount_amount=50.0,
            min_transaction_amount=100.0,
            start_date=datetime.now(),
            expiry_date=datetime(2025, 12, 31),
            terms_and_conditions="Valid until Dec 31, 2025"
        )

        offer_result = await client.call_tool("create_offer", offer=offer_data.model_dump())
        print(f"Offer created: {offer_result.content}")

        # Test merchant analytics
        print("\n📊 Testing merchant analytics:")
        analytics_result = await client.call_tool("get_merchant_analytics", merchant_id=1)
        print(f"Merchant analytics: {analytics_result.content}")

        # Test rewards balance
        print("\n🏆 Testing customer rewards balance:")
        rewards_result = await client.call_tool("get_customer_reward_balance", customer_id=1)
        print(f"Rewards balance: {rewards_result.content}")

async def main():
    """Main function to run the client tests"""
    try:
        await test_tools()
        print("\n✅ All tests completed successfully!")
    except Exception as e:
        print(f"❌ Error during testing: {e}")

if __name__ == "__main__":
    asyncio.run(main())
