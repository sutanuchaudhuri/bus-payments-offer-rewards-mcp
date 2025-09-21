"""
Advanced Pydantic client demonstrating type-safe interactions with the MCP server
"""
import asyncio
from fastmcp import Client
from models import (
    CustomerCreate, CustomerUpdate,
    MerchantCreate, PaymentCreate,
    OfferCreate, CreditCardCreate,
    RedeemPointsRequest, OfferActivationRequest,
    MerchantCategory, ProductType
)
from datetime import datetime, timedelta
from typing import List, Dict, Any

class PaymentSystemClient:
    """Type-safe client for the Chase Payments Rewards Offers MCP server"""

    def __init__(self):
        self.client = Client("stdio", command=["python", "main.py"])

    async def __aenter__(self):
        await self.client.__aenter__()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.__aexit__(exc_type, exc_val, exc_tb)

    async def create_complete_customer_profile(self, customer_data: CustomerCreate) -> Dict[str, Any]:
        """Create a customer and return the complete profile"""
        result = await self.client.call_tool("create_customer", customer=customer_data.model_dump())
        return result.content

    async def add_customer_credit_card(self, customer_id: int, card_data: CreditCardCreate) -> Dict[str, Any]:
        """Add a credit card to a customer account with full validation"""
        result = await self.client.call_tool(
            "add_credit_card",
            customer_id=customer_id,
            card=card_data.model_dump()
        )
        return result.content

    async def process_transaction(self, payment_data: PaymentCreate) -> Dict[str, Any]:
        """Process a payment transaction with rewards calculation"""
        result = await self.client.call_tool("make_payment", payment=payment_data.model_dump())
        return result.content

    async def create_promotional_offer(self, offer_data: OfferCreate) -> Dict[str, Any]:
        """Create a new promotional offer with validation"""
        result = await self.client.call_tool("create_offer", offer=offer_data.model_dump())
        return result.content

    async def activate_customer_offer(self, offer_id: int, customer_id: int) -> Dict[str, Any]:
        """Activate an offer for a specific customer"""
        activation_request = OfferActivationRequest(customer_id=customer_id)
        result = await self.client.call_tool(
            "activate_offer",
            offer_id=offer_id,
            request=activation_request.model_dump()
        )
        return result.content

    async def redeem_customer_points(self, customer_id: int, points: int, description: str = None) -> Dict[str, Any]:
        """Redeem reward points for a customer"""
        redemption_request = RedeemPointsRequest(points=points, description=description)
        result = await self.client.call_tool(
            "redeem_points",
            customer_id=customer_id,
            request=redemption_request.model_dump()
        )
        return result.content

async def demo_pydantic_workflow():
    """Demonstrate a complete workflow using Pydantic models"""

    async with PaymentSystemClient() as payment_client:
        print("🚀 Starting Pydantic-powered payment system workflow...")

        # 1. Create a new customer with validated data
        print("\n👤 Step 1: Creating customer with Pydantic validation")
        customer = CustomerCreate(
            first_name="Sarah",
            last_name="Johnson",
            email="sarah.johnson@email.com",
            phone="+1-555-0199",
            date_of_birth="1990-05-15",
            address="456 Oak Avenue, Seattle, WA 98101"
        )

        customer_result = await payment_client.create_complete_customer_profile(customer)
        print(f"✅ Customer created: {customer_result}")

        # 2. Add a credit card with type-safe enums
        print("\n💳 Step 2: Adding credit card with validated product type")
        credit_card = CreditCardCreate(
            card_number="4111111111111111",
            card_holder_name="Sarah Johnson",
            expiry_month=12,
            expiry_year=2028,
            product_type=ProductType.PLATINUM,  # Using Pydantic enum
            credit_limit=15000.00
        )

        card_result = await payment_client.add_customer_credit_card(1, credit_card)
        print(f"✅ Credit card added: {card_result}")

        # 3. Create a merchant with category validation
        print("\n🏪 Step 3: Creating merchant with category validation")
        merchant = MerchantCreate(
            merchant_id="STARBUCKS_001",
            name="Starbucks Coffee",
            description="Premium coffee chain",
            category=MerchantCategory.RESTAURANT,  # Using Pydantic enum
            website="https://starbucks.com",
            contact_email="business@starbucks.com",
            phone="+1-800-STARBUCKS",
            address="2401 Utah Avenue South, Seattle, WA 98134"
        )

        # Note: This would need to be implemented in the client
        print("✅ Merchant data validated with Pydantic")

        # 4. Create a promotional offer with date validation
        print("\n🎯 Step 4: Creating promotional offer with date validation")
        offer = OfferCreate(
            title="Coffee Lover's Bonus",
            description="Earn double points on all coffee purchases",
            category="BEVERAGE",
            merchant_id=1,
            discount_percentage=15.0,
            max_discount_amount=25.0,
            min_transaction_amount=10.0,
            reward_points=100,
            start_date=datetime.now(),
            expiry_date=datetime.now() + timedelta(days=30),
            terms_and_conditions="Valid for 30 days from activation"
        )

        offer_result = await payment_client.create_promotional_offer(offer)
        print(f"✅ Offer created: {offer_result}")

        # 5. Activate the offer for the customer
        print("\n🔗 Step 5: Activating offer for customer")
        activation_result = await payment_client.activate_customer_offer(1, 1)
        print(f"✅ Offer activated: {activation_result}")

        # 6. Process a payment transaction
        print("\n💰 Step 6: Processing payment with validation")
        payment = PaymentCreate(
            credit_card_id=1,
            amount=45.75,
            merchant_name="Starbucks Coffee",
            merchant_category="RESTAURANT",
            description="Morning coffee and pastries"
        )

        payment_result = await payment_client.process_transaction(payment)
        print(f"✅ Payment processed: {payment_result}")

        # 7. Redeem reward points
        print("\n🏆 Step 7: Redeeming reward points")
        redemption_result = await payment_client.redeem_customer_points(
            customer_id=1,
            points=50,
            description="Redeemed for gift card"
        )
        print(f"✅ Points redeemed: {redemption_result}")

        print("\n🎉 Complete Pydantic workflow demonstration finished!")

if __name__ == "__main__":
    asyncio.run(demo_pydantic_workflow())
