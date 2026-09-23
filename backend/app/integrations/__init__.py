"""External API integrations module package exports."""

from app.integrations.base import BaseIntegrationClient
from app.integrations.flights import FlightProvider, flight_provider
from app.integrations.hotels import HotelProvider, hotel_provider
from app.integrations.maps import MapsProvider, maps_provider
from app.integrations.weather import WeatherProvider, weather_provider
from app.integrations.notifications import (
    NotificationProvider,
    notification_provider,
)

__all__ = [
    "BaseIntegrationClient",
    "FlightProvider",
    "flight_provider",
    "HotelProvider",
    "hotel_provider",
    "MapsProvider",
    "maps_provider",
    "WeatherProvider",
    "weather_provider",
    "NotificationProvider",
    "notification_provider",
]
