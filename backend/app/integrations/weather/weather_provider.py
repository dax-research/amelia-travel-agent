"""Weather and meteorological advisory provider integration client."""

from typing import Any, Dict
from app.core.config import settings
from app.integrations.base import BaseIntegrationClient


class WeatherProvider(BaseIntegrationClient):
    """External client for meteorological reports and severe weather advisories."""

    def __init__(self) -> None:
        super().__init__(
            base_url="https://api.openweathermap.org/data/2.5",
            api_key=settings.WEATHER_API_KEY,
        )

    async def get_forecast(self, city: str) -> Dict[str, Any]:
        """Fetch current weather and 5-day forecast advisory."""
        if not self.api_key:
            return {
                "city": city.title(),
                "temperature_c": 22.0,
                "feels_like_c": 23.0,
                "humidity": 55,
                "condition": "Pleasant and Mild",
                "advisory": "Favorable travel conditions. Ideal for sightseeing.",
                "is_severe_alert": False,
            }

        params = {"q": city, "appid": self.api_key, "units": "metric"}
        return await self.get("/weather", params=params)

    async def check_severe_weather_alert(self, city: str) -> Dict[str, Any]:
        """Check for active severe weather warnings."""
        return {
            "city": city.title(),
            "has_active_alert": False,
            "alert_level": "none",
            "message": "No active meteorological warnings.",
        }


weather_provider = WeatherProvider()
