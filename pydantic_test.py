import asyncio
from fastmcp import Client
from models import CustomerCreate, PaymentCreate, OfferCreate
from datetime import datetime
from main import mcp
import sys

async def test_pydantic_tools():
    """Test FastMCP tools with Pydantic models and verbose output"""

    print("🚀 Starting Pydantic FastMCP Client Test", flush=True)

    try:
        # Create client connection directly to the FastMCP server instance
        async with Client(mcp) as client:
            print("🔌 Successfully connected to ChasePaymentsRewardsOffers MCP Server", flush=True)

            # List all available tools
            print("\n📋 Listing all available tools:", flush=True)
            tools = await client.list_tools()
            print(f"Found tools: {type(tools)}", flush=True)

            if hasattr(tools, 'tools'):
                tool_list = tools.tools
            else:
                tool_list = tools

            for i, tool in enumerate(tool_list):
                print(f"  {i+1}. {tool.name}: {tool.description[:100]}...", flush=True)

            print(f"\n✅ Total tools available: {len(tool_list)}", flush=True)

            # Test health check
            print("\n🏥 Testing health check tool:", flush=True)
            health_result = await client.call_tool("health_check")
            print(f"Health check result type: {type(health_result)}", flush=True)
            print(f"Health status response: {health_result}", flush=True)

            # Test customer creation with Pydantic model
            print("\n👤 Testing customer creation with Pydantic validation:", flush=True)
            customer_data = CustomerCreate(
                first_name="Alice",
                last_name="Smith",
                email="alice.smith@example.com",
                phone="+1-555-0199",
                address="789 Pine St, Boston, MA 02101"
            )

            print(f"Customer data created: {customer_data}", flush=True)
            print(f"Customer data as dict: {customer_data.model_dump()}", flush=True)

            customer_result = await client.call_tool("create_customer", arguments={"customer": customer_data.model_dump()})
            print(f"Customer creation response: {customer_result}", flush=True)

            # Test payment processing with Pydantic model
            print("\n💳 Testing payment processing with validation:", flush=True)
            payment_data = PaymentCreate(
                credit_card_id=1,
                amount=125.50,
                merchant_name="Starbucks",
                merchant_category="RESTAURANT",
                description="Coffee and breakfast"
            )

            print(f"Payment data: {payment_data.model_dump()}", flush=True)
            payment_result = await client.call_tool("make_payment", arguments={"payment": payment_data.model_dump()})
            print(f"Payment result: {payment_result}", flush=True)

            # Test offer creation with Pydantic model and date validation
            print("\n🎯 Testing offer creation with date validation:", flush=True)
            offer_data = OfferCreate(
                title="Coffee Rewards",
                description="Earn 2x points on coffee purchases",
                category="BEVERAGE",
                discount_percentage=10.0,
                max_discount_amount=15.0,
                min_transaction_amount=5.0,
                start_date=datetime.now(),
                expiry_date=datetime(2025, 12, 31),
                terms_and_conditions="Valid at participating locations"
            )

            print(f"Offer data: {offer_data.model_dump()}", flush=True)
            offer_result = await client.call_tool("create_offer", arguments={"offer": offer_data.model_dump()})
            print(f"Offer creation result: {offer_result}", flush=True)

            print("\n🎉 All Pydantic validation tests completed successfully!", flush=True)

    except Exception as e:
        print(f"❌ Error during testing: {e}", flush=True)
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Starting Pydantic FastMCP test...", flush=True)
    asyncio.run(test_pydantic_tools())
    print("Test completed.", flush=True)
