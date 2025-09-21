from pydantic import BaseModel, Field
from .enums import ProductType

class CreditCardCreate(BaseModel):
    """Credit card creation request model"""
    card_number: str = Field(..., description="Credit card number")
    card_holder_name: str = Field(..., description="Name on the card")
    expiry_month: int = Field(..., description="Card expiry month", ge=1, le=12)
    expiry_year: int = Field(..., description="Card expiry year")
    product_type: ProductType = Field(..., description="Card product type")
    credit_limit: float = Field(..., description="Credit limit amount", gt=0)
