from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Customer(BaseModel):
    """Customer entity model"""
    id: int = Field(..., description="Unique customer identifier")
    first_name: str = Field(..., description="Customer's first name")
    last_name: str = Field(..., description="Customer's last name")
    email: str = Field(..., description="Customer's email address")
    phone: Optional[str] = Field(None, description="Customer's phone number")
    date_of_birth: Optional[str] = Field(None, description="Customer's date of birth")
    address: Optional[str] = Field(None, description="Customer's address")
    created_at: Optional[datetime] = Field(None, description="Account creation timestamp")
    updated_at: Optional[datetime] = Field(None, description="Last update timestamp")

class CustomerCreate(BaseModel):
    """Customer creation request model"""
    first_name: str = Field(..., description="Customer's first name")
    last_name: str = Field(..., description="Customer's last name")
    email: str = Field(..., description="Customer's email address")
    phone: Optional[str] = Field(None, description="Customer's phone number")
    date_of_birth: Optional[str] = Field(None, description="Customer's date of birth")
    address: Optional[str] = Field(None, description="Customer's address")

class CustomerUpdate(BaseModel):
    """Customer update request model"""
    first_name: Optional[str] = Field(None, description="Customer's first name")
    last_name: Optional[str] = Field(None, description="Customer's last name")
    email: Optional[str] = Field(None, description="Customer's email address")
    phone: Optional[str] = Field(None, description="Customer's phone number")
    date_of_birth: Optional[str] = Field(None, description="Customer's date of birth")
    address: Optional[str] = Field(None, description="Customer's address")
