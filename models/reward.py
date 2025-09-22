from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from .enums import RewardStatus

class Reward(BaseModel):
    """Reward entity model"""
    id: int = Field(..., description="Unique reward identifier")
    customer_id: int = Field(..., description="Customer who earned the reward")
    payment_id: Optional[int] = Field(None, description="Associated payment ID")
    offer_id: Optional[int] = Field(None, description="Associated offer ID")
    points_earned: Optional[int] = Field(None, description="Points earned")
    points_redeemed: Optional[int] = Field(None, description="Points redeemed")
    dollar_value: Optional[float] = Field(None, description="Dollar value of reward")
    status: RewardStatus = Field(..., description="Reward status")
    earned_date: Optional[datetime] = Field(None, description="Date reward was earned")
    redeemed_date: Optional[datetime] = Field(None, description="Date reward was redeemed")
    expiry_date: Optional[datetime] = Field(None, description="Reward expiry date")
    description: Optional[str] = Field(None, description="Reward description")

class RewardCreate(BaseModel):
    """Manual reward creation request model"""
    customer_id: int = Field(..., description="Customer ID")
    points_earned: int = Field(..., description="Points to award", ge=1)
    description: str = Field(..., description="Reward description")
    offer_id: Optional[int] = Field(None, description="Associated offer ID")
    dollar_value: Optional[float] = Field(None, description="Dollar value of reward")
    expiry_date: Optional[datetime] = Field(None, description="Reward expiry date")

class RedeemPointsRequest(BaseModel):
    """Redeem points request model"""
    points: int = Field(..., description="Number of points to redeem", ge=1)
    description: Optional[str] = Field(None, description="Description of redemption")

class RewardRedemption(BaseModel):
    """Reward redemption model"""
    points: Optional[int] = Field(None, description="Points to redeem from specific reward", ge=1)

class CustomerBalance(BaseModel):
    """Customer points balance model"""
    customer_id: int = Field(..., description="Customer ID")
    total_points_earned: int = Field(..., description="Total points earned")
    total_points_redeemed: int = Field(..., description="Total points redeemed")
    available_points: int = Field(..., description="Available points balance")
    pending_points: int = Field(..., description="Pending points")
    expired_points: int = Field(..., description="Expired points")

class RewardListResponse(BaseModel):
    """Response model for reward list"""
    rewards: List[Reward] = Field(..., description="List of rewards")
    total: int = Field(..., description="Total number of rewards")
    pages: int = Field(..., description="Total pages")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")

class RedemptionHistory(BaseModel):
    """Redemption history model"""
    redemptions: List[dict] = Field(..., description="List of redemptions")
    total: int = Field(..., description="Total redemptions")
    pages: int = Field(..., description="Total pages")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")
