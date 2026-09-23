"""API v1 routers export."""

from app.api.v1.health import router as health_router
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.trips import router as trips_router
from app.api.v1.itinerary import router as itinerary_router
from app.api.v1.flights import router as flights_router
from app.api.v1.hotels import router as hotels_router
from app.api.v1.bookings import router as bookings_router
from app.api.v1.notifications import router as notifications_router
from app.api.v1.agent import router as agent_router

__all__ = [
    "health_router",
    "auth_router",
    "users_router",
    "trips_router",
    "itinerary_router",
    "flights_router",
    "hotels_router",
    "bookings_router",
    "notifications_router",
    "agent_router",
]
