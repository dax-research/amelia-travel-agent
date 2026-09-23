"""Central API router mounting all modular domain route collections."""

from fastapi import APIRouter

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

api_router = APIRouter()

# Mount all domain routers
api_router.include_router(health_router)
api_router.include_router(auth_router)
api_router.include_router(users_router)
api_router.include_router(trips_router)
api_router.include_router(itinerary_router)
api_router.include_router(flights_router)
api_router.include_router(hotels_router)
api_router.include_router(bookings_router)
api_router.include_router(notifications_router)
api_router.include_router(agent_router)
