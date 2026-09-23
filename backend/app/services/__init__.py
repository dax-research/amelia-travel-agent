"""Services package exports."""

from app.services.base import BaseService
from app.services.auth_service import AuthService, auth_service
from app.services.user_service import UserService, user_service
from app.services.trip_service import TripService, trip_service
from app.services.itinerary_service import ItineraryService, itinerary_service
from app.services.flight_service import FlightService, flight_service
from app.services.hotel_service import HotelService, hotel_service
from app.services.booking_service import BookingService, booking_service
from app.services.notification_service import NotificationService, notification_service
from app.services.agent_service import AgentService, agent_service

__all__ = [
    "BaseService",
    "AuthService",
    "auth_service",
    "UserService",
    "user_service",
    "TripService",
    "trip_service",
    "ItineraryService",
    "itinerary_service",
    "FlightService",
    "flight_service",
    "HotelService",
    "hotel_service",
    "BookingService",
    "booking_service",
    "NotificationService",
    "notification_service",
    "AgentService",
    "agent_service",
]
