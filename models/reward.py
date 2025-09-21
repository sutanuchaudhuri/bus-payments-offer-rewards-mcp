from pydantic import BaseModel, Field
from typing import Optional
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

class RedeemPointsRequest(BaseModel):
    """Redeem points request model"""
    points: int = Field(..., description="Number of points to redeem", gt=0)
    description: Optional[str] = Field(None, description="Description of redemption")
