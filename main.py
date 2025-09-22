from fastmcp import FastMCP
from tools import register_all_tools
from fastmcp.server.auth import JWTVerifier
from fastmcp.server.auth.providers.jwt import RSAKeyPair
import random

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
    mcp.run(transport="sse")
    # mcp.run(transport="http", port=8000)

    # In a real implementation, you might want to run this differently
    # For now, this shows the server is configured and ready
    print("MCP Server initialized successfully!")
    print("ChasePaymentsRewardsOffers server is ready to handle requests.")

    # The server is now ready to be used by MCP clients
    # In production, you would typically run this with: python -m fastmcp main:mcp
