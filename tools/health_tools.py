from fastmcp import FastMCP
from models import api_client

def register_health_tools(mcp: FastMCP):
    """Register health-related MCP tools"""
    
    @mcp.tool(
        name="health_check",
        description="Perform a comprehensive health check of the credit card payment system API. Returns current system status, timestamp, and operational readiness indicators for monitoring and diagnostics.",
        tags={"health", "monitoring", "diagnostics", "system_status"},
        meta={"version": "1.0", "category": "system_health"}
    )
    async def health_check() -> dict:
        """Health check endpoint to verify API status"""
        return await api_client.get("/api/health")
