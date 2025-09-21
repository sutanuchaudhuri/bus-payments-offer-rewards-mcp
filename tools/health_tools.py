from fastmcp import FastMCP
from datetime import datetime
from models import HealthResponse

def register_health_tools(mcp: FastMCP):
    """Register health-related MCP tools"""

    @mcp.tool(
        name="health_check",
        description="Perform a comprehensive health check of the credit card payment system API. Returns current system status, timestamp, and operational readiness indicators for monitoring and diagnostics.",
        tags={"health", "monitoring", "diagnostics", "system_status"},
        meta={"version": "1.0", "category": "system_health"}
    )
    async def health_check() -> HealthResponse:
        """Health check endpoint to verify API status"""
        return HealthResponse(status="healthy", timestamp=datetime.utcnow())
