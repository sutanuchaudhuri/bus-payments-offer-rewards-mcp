import os
import httpx
from typing import Optional, Dict, Any, Union
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class APIClient:
    """Base API client for making HTTP requests to the bus payments API"""

    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL", "http://192.168.86.189:5001")
        self.timeout = 30.0

    async def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Make an HTTP request to the API"""
        url = f"{self.base_url}{endpoint}"

        default_headers = {"Content-Type": "application/json"}
        if headers:
            default_headers.update(headers)

        async with httpx.AsyncClient(timeout=self.timeout) as client:
            response = await client.request(
                method=method,
                url=url,
                params=params,
                json=json_data,
                headers=default_headers
            )

            # Check if response is successful
            if response.status_code >= 400:
                error_detail = f"HTTP {response.status_code}"
                try:
                    error_data = response.json()
                    if "error" in error_data:
                        error_detail = error_data["error"]
                    elif "message" in error_data:
                        error_detail = error_data["message"]
                except:
                    error_detail = response.text or error_detail

                raise Exception(f"API Error: {error_detail}")

            # Return JSON response
            try:
                return response.json()
            except:
                return {"message": "Success", "status_code": response.status_code}

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a GET request"""
        return await self._make_request("GET", endpoint, params=params)

    async def post(self, endpoint: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a POST request"""
        return await self._make_request("POST", endpoint, params=params, json_data=data)

    async def put(self, endpoint: str, data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a PUT request"""
        return await self._make_request("PUT", endpoint, params=params, json_data=data)

    async def delete(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make a DELETE request"""
        return await self._make_request("DELETE", endpoint, params=params)

# Global API client instance
api_client = APIClient()
