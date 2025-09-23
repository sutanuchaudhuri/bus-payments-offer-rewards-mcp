from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime, date

class Customer(BaseModel):
    """Customer entity representing an individual user of the payment system."""
    id: Optional[int] = Field(None, description="Internal database ID (auto-generated)")
    customer_id: str = Field(..., description="Alphanumeric customer identifier used for all API operations.")
    first_name: str = Field(..., max_length=100, description="Customer's first name")
    last_name: str = Field(..., max_length=100, description="Customer's last name")
    email: EmailStr = Field(..., max_length=255, description="Customer's email address (must be unique)")
    phone: Optional[str] = Field(None, max_length=20, description="Customer's phone number")
    date_of_birth: Optional[date] = Field(None, description="Customer's date of birth")
    address: Optional[str] = Field(None, description="Customer's mailing address")
    created_at: Optional[datetime] = Field(None, description="Customer creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")

class CustomerCreate(BaseModel):
    """Request payload for creating a new customer"""
    first_name: str = Field(..., max_length=100, description="Customer's first name")
    last_name: str = Field(..., max_length=100, description="Customer's last name")
    email: EmailStr = Field(..., max_length=255, description="Customer's email address")
    phone: Optional[str] = Field(None, max_length=20, description="Customer's phone number")
    date_of_birth: Optional[date] = Field(None, description="Customer's date of birth")
    address: Optional[str] = Field(None, description="Customer's address")

class CustomerUpdate(BaseModel):
    """Request payload for updating a customer"""
    first_name: Optional[str] = Field(None, max_length=100, description="Customer's first name")
    last_name: Optional[str] = Field(None, max_length=100, description="Customer's last name")
    email: Optional[EmailStr] = Field(None, max_length=255, description="Customer's email address")
    phone: Optional[str] = Field(None, max_length=20, description="Customer's phone number")
    date_of_birth: Optional[date] = Field(None, description="Customer's date of birth")
    address: Optional[str] = Field(None, description="Customer's address")

class CustomerListResponse(BaseModel):
    """Paginated list of customers with metadata"""
    customers: List[Customer] = Field(..., description="List of customers")
    total: int = Field(..., description="Total number of customers in system")
    pages: int = Field(..., description="Total number of pages available")
    current_page: int = Field(..., description="Current page number")
    per_page: int = Field(..., description="Number of customers per page")
