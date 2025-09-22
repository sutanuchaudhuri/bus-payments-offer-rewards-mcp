from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict
from datetime import datetime

# Health Response Model
class HealthResponse(BaseModel):
    """Health check response model"""
    status: str = Field(..., description="API health status", json_schema_extra={"example": "healthy"})
    timestamp: datetime = Field(..., description="Current timestamp")

# Generic Success Response
class SuccessResponse(BaseModel):
    """Generic success response model"""
    message: str = Field(..., description="Success message")
    data: Optional[Dict[str, Any]] = Field(None, description="Additional response data")

# Error Response Model
class ErrorResponse(BaseModel):
    """Error response model"""
    error: str = Field(..., description="Error message")
    details: Optional[str] = Field(None, description="Additional error details")
    code: Optional[int] = Field(None, description="Error code")

# Payment Response Model
class PaymentResponse(BaseModel):
    """Payment processing response model"""
    payment_id: int = Field(..., description="Created payment ID")
    status: str = Field(..., description="Payment status")
    amount: float = Field(..., description="Payment amount")
    rewards_earned: int = Field(..., description="Rewards points earned")
    offers_applied: List[str] = Field(..., description="List of offers applied")

# Reward Balance Response Model
class RewardBalanceResponse(BaseModel):
    """Reward balance response model"""
    customer_id: int = Field(..., description="Customer ID")
    total_points: int = Field(..., description="Total points earned")
    available_points: int = Field(..., description="Available points for redemption")
    dollar_value: float = Field(..., description="Dollar value of available points")

# Analytics Response Models
class MerchantAnalyticsResponse(BaseModel):
    """Merchant analytics response model"""
    merchant_id: int = Field(..., description="Merchant ID")
    total_transactions: int = Field(..., description="Total number of transactions")
    total_amount: float = Field(..., description="Total transaction amount")
    period: str = Field(..., description="Analytics period")

# Profile History Response Model
class ProfileHistoryResponse(BaseModel):
    """Profile history response model"""
    customer_id: int = Field(..., description="Customer ID")
    changes: List[Dict[str, Any]] = Field(..., description="List of profile changes")
    total: int = Field(..., description="Total number of changes")
