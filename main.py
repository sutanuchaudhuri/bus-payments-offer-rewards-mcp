from fastmcp import FastMCP
from tools import register_all_tools
from fastmcp.server.auth import JWTVerifier
from fastmcp.server.auth.providers.jwt import RSAKeyPair
import random
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

key_pair = RSAKeyPair.generate()
access_token = key_pair.create_token(audience="ChasePaymentsRewardsOffersMCPServer")

auth = JWTVerifier(
    public_key=key_pair.public_key,
    audience="ChasePaymentsRewardsOffersMCPServer",
)

# Initialize FastMCP server
mcp = FastMCP(name="ChasePaymentsRewardsOffersMCPServer",
              instructions="""Credit Card Payment System API including
              Payments
              Offers
              Rewards
              Disputes
              Live Check with Merchants
              """,
              auth=None
              )

# Register all tools from the tools package
register_all_tools(mcp)

if __name__ == "__main__":
    # Run the MCP server
    print("Starting Credit Card Payment System MCP Server...")
    print("Available tools have been registered and are ready for use.")

    # Read port and transport from environment variables with defaults
    port = int(os.getenv("PORT", 8001))
    transport = os.getenv("TRANSPORT", "sse")
    print(f"Starting server with transport '{transport}' on port {port}")

    mcp.run(transport=transport, port=port)

    # In a real implementation, you might want to run this differently
    # For now, this shows the server is configured and ready
    print("MCP Server initialized successfully!")
    print("ChasePaymentsRewardsOffers server is ready to handle requests.")

    # The server is now ready to be used by MCP clients
    # In production, you would typically run this with: python -m fastmcp main:mcp
