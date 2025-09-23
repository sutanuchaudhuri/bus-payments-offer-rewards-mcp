# Enums
from .enums import *
from .base_client import api_client, APIClient

# Entity Models - cleaned up to match swagger.json exactly
from .customer import Customer, CustomerCreate, CustomerUpdate, CustomerListResponse
from .credit_card import CreditCard, CreditCardCreate, CreditCardUpdate, CreditCardListResponse
from .merchant import (
    Merchant, MerchantCreate, MerchantUpdate, MerchantListResponse,
    MerchantCategoryInfo, MerchantCategoriesResponse, MerchantAnalytics
)
from .offer import (
    Offer, OfferCreate, OfferUpdate, OfferActivationRequest, OfferActivation,
    OfferListResponse, OfferCategoryInfo, OfferStatistics
)
from .payment import (
    Payment, PaymentCreate, PaymentRefund, PaymentListResponse, SpendingAnalytics
)
from .reward import (
    Reward, RewardCreate, RedeemPointsRequest, RewardRedemption, CustomerBalance,
    RewardListResponse, RedemptionHistory
)
from .refund import (
    Refund, RefundRequest, PointsRefundRequest, RefundApproval, RefundDenial,
    RefundListResponse
)
# Minimal booking models - only 2 API endpoints exist
from .booking import BookingModification, BookingStatusResponse

# Integration models - reorganized by functionality
from .integrations import (
    # Token management
    CardToken, CardTokenRequest, TokenValidationResponse,
    # Travel integrations (/offers/ endpoints)
    HotelSearchRequest, HotelBookingRequest, FlightSearchRequest, FlightBookingRequest,
    TravelPackageSearchRequest,
    # Shopping integrations (/offers/ endpoints)
    ShoppingProductSearch, ShoppingCartItem, ShoppingOrder,
    # System status
    IntegrationStatus
)

# Response Models
from .responses import *

__all__ = [
    # Enums - cleaned up, removed TokenType as not in swagger schemas
    "BookingStatus", "CreditCardProduct", "MerchantCategory", "OfferCategory",
    "PaymentStatus", "RefundStatus", "RefundType", "RewardStatus",

    # Client
    "api_client", "APIClient",

    # Customer models
    "Customer", "CustomerCreate", "CustomerUpdate", "CustomerListResponse",

    # Credit Card models
    "CreditCard", "CreditCardCreate", "CreditCardUpdate", "CreditCardListResponse",

    # Merchant models
    "Merchant", "MerchantCreate", "MerchantUpdate", "MerchantListResponse",
    "MerchantCategoryInfo", "MerchantCategoriesResponse", "MerchantAnalytics",

    # Offer models
    "Offer", "OfferCreate", "OfferUpdate", "OfferActivationRequest", "OfferActivation",
    "OfferListResponse", "OfferCategoryInfo", "OfferStatistics",

    # Payment models
    "Payment", "PaymentCreate", "PaymentRefund", "PaymentListResponse", "SpendingAnalytics",

    # Reward models
    "Reward", "RewardCreate", "RedeemPointsRequest", "RewardRedemption", "CustomerBalance",
    "RewardListResponse", "RedemptionHistory",

    # Refund models
    "Refund", "RefundRequest", "PointsRefundRequest", "RefundApproval", "RefundDenial",
    "RefundListResponse",

    # Minimal booking models - only 2 endpoints exist
    "BookingModification", "BookingStatusResponse",

    # Integration models - reorganized by functionality
    # Token management
    "CardToken", "CardTokenRequest", "TokenValidationResponse",
    # Travel integrations
    "HotelSearchRequest", "HotelBookingRequest", "FlightSearchRequest", "FlightBookingRequest",
    "TravelPackageSearchRequest",
    # Shopping integrations
    "ShoppingProductSearch", "ShoppingCartItem", "ShoppingOrder",
    # System status
    "IntegrationStatus",
]
