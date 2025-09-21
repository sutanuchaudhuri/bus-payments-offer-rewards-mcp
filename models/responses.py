from pydantic import BaseModel, Field
from typing import List
from .customer import Customer
from .merchant import Merchant
from .payment import Payment
from .offer import Offer
from .reward import Reward
from .profile_history import CustomerProfileHistory
from datetime import datetime

# Health Response Model
class HealthResponse(BaseModel):
    """Health check response model"""
    status: str = Field(..., description="API health status", example="healthy")
    timestamp: datetime = Field(..., description="Current timestamp")

# List Response Models
class CustomerListResponse(BaseModel):
    """Customer list response model"""
    customers: List[Customer] = Field(..., description="List of customers")
    total: int = Field(..., description="Total number of customers")
    page: int = Field(..., description="Current page number")
    per_page: int = Field(..., description="Items per page")
    pages: int = Field(..., description="Total number of pages")

class MerchantListResponse(BaseModel):
    """Merchant list response model"""
    merchants: List[Merchant] = Field(..., description="List of merchants")
    total: int = Field(..., description="Total number of merchants")

class PaymentListResponse(BaseModel):
    """Payment list response model"""
    payments: List[Payment] = Field(..., description="List of payments")
    total: int = Field(..., description="Total number of payments")

class OfferListResponse(BaseModel):
    """Offer list response model"""
    offers: List[Offer] = Field(..., description="List of offers")

class RewardListResponse(BaseModel):
    """Reward list response model"""
    rewards: List[Reward] = Field(..., description="List of rewards")

# Complex Response Models
class RewardBalanceResponse(BaseModel):
    """Reward balance response model"""
    total_points: int = Field(..., description="Total points earned")
    available_points: int = Field(..., description="Available points for redemption")
    dollar_value: float = Field(..., description="Dollar value of available points")

class ProfileHistoryResponse(BaseModel):
    """Profile history response model"""
    history: List[CustomerProfileHistory] = Field(..., description="List of profile history records")

class CustomerProfileHistoryResponse(BaseModel):
    """Customer profile history response model"""
    history: List[CustomerProfileHistory] = Field(..., description="List of profile history records")
    total_saved: float = Field(..., description="Total amount saved by customer")

class PaymentResponse(BaseModel):
    """Payment processing response model"""
    payment: Payment = Field(..., description="Payment details")
    rewards_earned: int = Field(..., description="Rewards points earned")
    offers_applied: List[dict] = Field(..., description="Offers applied to this payment")

class MerchantAnalyticsResponse(BaseModel):
    """Merchant analytics response model"""
    total_transactions: int = Field(..., description="Total number of transactions")
    total_amount: float = Field(..., description="Total transaction amount")
    total_discounts: float = Field(..., description="Total discounts given")
    active_offers: int = Field(..., description="Number of active offers")
