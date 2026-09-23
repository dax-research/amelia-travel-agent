"""Pydantic schemas package exports."""

from app.schemas.common import (
    ApiResponse,
    ErrorDetail,
    ErrorResponse,
    PaginatedResponse,
    PaginationParams,
)
from app.schemas.auth import (
    Token,
    TokenPayload,
    UserBase,
    UserLogin,
    UserRegister,
    UserResponse,
)
from app.schemas.user import (
    UserProfile,
    UserProfileUpdate,
    TravelPreferences,
)
from app.schemas.trip import (
    ItineraryDay,
    ItineraryItem,
    TripBase,
    TripCreate,
    TripResponse,
    TripUpdate,
)
from app.schemas.itinerary import (
    ItineraryDayDetail,
    ItineraryGenerateRequest,
    ItineraryItemBase,
    ItineraryItemCreate,
    ItineraryItemUpdate,
    ItineraryResponse,
)
from app.schemas.flight import (
    FlightOffer,
    FlightSearchQuery,
    FlightSegment,
    FlightStatus,
)
from app.schemas.hotel import (
    HotelOffer,
    HotelRoom,
    HotelSearchQuery,
)
from app.schemas.booking import (
    BookingCreate,
    BookingResponse,
    BookingStatus,
    BookingType,
)
from app.schemas.notification import (
    NotificationChannel,
    NotificationCreate,
    NotificationPriority,
    NotificationResponse,
)
from app.schemas.agent import (
    AgentMessage,
    AgentQueryRequest,
    AgentQueryResponse,
    TravelSafetyAlert,
)

__all__ = [
    "ApiResponse",
    "ErrorDetail",
    "ErrorResponse",
    "PaginationParams",
    "PaginatedResponse",
    "UserBase",
    "UserRegister",
    "UserLogin",
    "UserResponse",
    "Token",
    "TokenPayload",
    "UserProfile",
    "UserProfileUpdate",
    "TravelPreferences",
    "TripBase",
    "TripCreate",
    "TripUpdate",
    "TripResponse",
    "ItineraryDay",
    "ItineraryItem",
    "ItineraryDayDetail",
    "ItineraryItemBase",
    "ItineraryItemCreate",
    "ItineraryItemUpdate",
    "ItineraryGenerateRequest",
    "ItineraryResponse",
    "FlightSearchQuery",
    "FlightSegment",
    "FlightOffer",
    "FlightStatus",
    "HotelSearchQuery",
    "HotelRoom",
    "HotelOffer",
    "BookingType",
    "BookingStatus",
    "BookingCreate",
    "BookingResponse",
    "NotificationPriority",
    "NotificationChannel",
    "NotificationCreate",
    "NotificationResponse",
    "AgentMessage",
    "AgentQueryRequest",
    "AgentQueryResponse",
    "TravelSafetyAlert",
]
