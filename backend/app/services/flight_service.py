"""Business logic service for flight operations and status tracking."""

from typing import Any, Dict, List
from app.integrations.flights import flight_provider
from app.schemas.flight import FlightOffer, FlightSearchQuery, FlightStatus
from app.services.base import BaseService


class FlightService(BaseService):
    """Coordinates flight offer searches, price comparisons, and operational alerts."""

    async def search_flights(self, query: FlightSearchQuery) -> List[Dict[str, Any]]:
        """Query external providers for available flight routes."""
        self.log_action("search_flights", {"origin": query.origin, "destination": query.destination})
        return await flight_provider.search_flights(
            origin=query.origin,
            destination=query.destination,
            departure_date=query.departure_date,
            passengers=query.passengers,
        )

    async def get_flight_status(self, flight_number: str) -> FlightStatus:
        """Fetch live operational status and assess disruption probability."""
        status_data = await flight_provider.get_flight_status(flight_number)
        return FlightStatus(**status_data)


flight_service = FlightService()
