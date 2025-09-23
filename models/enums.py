from enum import Enum

class BookingStatus(str, Enum):
    """External service booking status for travel and merchant integrations."""
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"
    COMPLETED = "COMPLETED"
    REFUNDED = "REFUNDED"

class CreditCardProduct(str, Enum):
    """Credit card product tiers determining reward multipliers and benefits."""
    BASIC = "BASIC"
    SILVER = "SILVER"
    GOLD = "GOLD"
    PLATINUM = "PLATINUM"

class MerchantCategory(str, Enum):
    """Merchant business categories for payment classification and offer targeting."""
    RESTAURANT = "RESTAURANT"
    RETAIL_STORE = "RETAIL_STORE"
    GAS_STATION = "GAS_STATION"
    AIRLINE = "AIRLINE"
    HOTEL = "HOTEL"
    E_COMMERCE = "E_COMMERCE"
    GROCERY_STORE = "GROCERY_STORE"
    PHARMACY = "PHARMACY"
    ENTERTAINMENT_VENUE = "ENTERTAINMENT_VENUE"
    HEALTHCARE_PROVIDER = "HEALTHCARE_PROVIDER"
    TELECOM_PROVIDER = "TELECOM_PROVIDER"
    UTILITY_COMPANY = "UTILITY_COMPANY"
    INSURANCE_COMPANY = "INSURANCE_COMPANY"
    EDUCATIONAL_INSTITUTION = "EDUCATIONAL_INSTITUTION"
    AUTOMOTIVE_SERVICE = "AUTOMOTIVE_SERVICE"
    HOME_IMPROVEMENT = "HOME_IMPROVEMENT"
    FASHION_RETAILER = "FASHION_RETAILER"
    ELECTRONICS_STORE = "ELECTRONICS_STORE"
    SUBSCRIPTION_SERVICE = "SUBSCRIPTION_SERVICE"
    FINANCIAL_SERVICE = "FINANCIAL_SERVICE"
    FITNESS_CENTER = "FITNESS_CENTER"

class OfferCategory(str, Enum):
    """Offer categories for targeted promotions and customer engagement."""
    TRAVEL = "TRAVEL"
    MERCHANT = "MERCHANT"
    CASHBACK = "CASHBACK"
    DINING = "DINING"
    FUEL = "FUEL"
    SHOPPING = "SHOPPING"
    GROCERY = "GROCERY"
    ENTERTAINMENT = "ENTERTAINMENT"
    HEALTH_WELLNESS = "HEALTH_WELLNESS"
    TELECOMMUNICATIONS = "TELECOMMUNICATIONS"
    UTILITIES = "UTILITIES"
    INSURANCE = "INSURANCE"
    EDUCATION = "EDUCATION"
    AUTOMOTIVE = "AUTOMOTIVE"
    HOME_GARDEN = "HOME_GARDEN"
    FASHION = "FASHION"
    ELECTRONICS = "ELECTRONICS"
    SUBSCRIPTION = "SUBSCRIPTION"
    FINANCE = "FINANCE"
    SPORTS_FITNESS = "SPORTS_FITNESS"

class PaymentStatus(str, Enum):
    """Payment transaction status lifecycle tracking."""
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    REFUNDED = "REFUNDED"

class RefundStatus(str, Enum):
    """Refund request processing status with defined workflow."""
    REQUESTED = "REQUESTED"
    APPROVED = "APPROVED"
    DENIED = "DENIED"
    PROCESSED = "PROCESSED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

class RefundType(str, Enum):
    """Types of refund requests supported by the system."""
    BOOKING_CANCELLATION = "booking_cancellation"
    DISPUTE_RESOLUTION = "dispute_resolution"
    GOODWILL = "goodwill"

class RewardStatus(str, Enum):
    """Reward points lifecycle status tracking."""
    EARNED = "EARNED"
    REDEEMED = "REDEEMED"
    EXPIRED = "EXPIRED"

# Alias for backward compatibility
ProductType = CreditCardProduct
