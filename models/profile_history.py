from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class CustomerProfileHistory(BaseModel):
    """Customer profile history entity model"""
    id: int = Field(..., description="Unique history record identifier")
    customer_id: int = Field(..., description="Customer identifier")
    customer_name: Optional[str] = Field(None, description="Customer name")
    merchant_id: Optional[int] = Field(None, description="Merchant identifier")
    merchant_name: Optional[str] = Field(None, description="Merchant name")
    offer_id: Optional[int] = Field(None, description="Offer identifier")
    offer_title: Optional[str] = Field(None, description="Offer title")
    payment_id: Optional[int] = Field(None, description="Payment identifier")
    amount_availed: Optional[float] = Field(None, description="Amount of discount/reward availed")
    transaction_amount: Optional[float] = Field(None, description="Transaction amount")
    savings_percentage: Optional[float] = Field(None, description="Savings percentage")
    statement_descriptor: Optional[str] = Field(None, description="Statement descriptor")
    availed_date: Optional[datetime] = Field(None, description="Date offer was availed")
    offer_category: Optional[str] = Field(None, description="Offer category")
    merchant_category: Optional[str] = Field(None, description="Merchant category")

class ProfileHistoryResponse(BaseModel):
    """Profile history list response model"""
    history: List[CustomerProfileHistory] = Field(..., description="List of profile history records")
    total: int = Field(..., description="Total number of records")
    pages: int = Field(..., description="Total pages")
    current_page: int = Field(..., description="Current page")
    per_page: int = Field(..., description="Items per page")

class CustomerProfileHistoryResponse(BaseModel):
    """Customer profile history response model"""
    customer_id: int = Field(..., description="Customer ID")
    history: List[CustomerProfileHistory] = Field(..., description="Customer's profile history")
    total_saved: float = Field(..., description="Total amount saved by customer")
    total_transactions: int = Field(..., description="Total number of transactions")
    total_offers_used: int = Field(..., description="Total offers utilized")
    average_savings_percentage: float = Field(..., description="Average savings percentage")
