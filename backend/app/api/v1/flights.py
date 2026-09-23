"""Flight search and live status tracking endpoints."""

from typing import Any, Dict, List
from fastapi import APIRouter, Query, status
from app.schemas.common import ApiResponse
from app.schemas.flight import FlightSearchQuery, FlightStatus
from app.services.flight_service import flight_service

router = APIRouter(prefix="/flights", tags=["Flights"])


@router.get(
    "/search",
    response_model=ApiResponse[List[Dict[str, Any]]],
    summary="Search flight offers",
)
async def search_flights(
    origin: str = Query(..., min_length=3, max_length=4, description="Departure IATA code (e.g. JFK)"),
    destination: str = Query(..., min_length=3, max_length=4, description="Arrival IATA code (e.g. LHR)"),
    departure_date: str = Query(..., description="Date YYYY-MM-DD"),
    passengers: int = Query(default=1, ge=1, le=9),
) -> ApiResponse[List[Dict[str, Any]]]:
    """Search available flights across multiple airline partners."""
    query = FlightSearchQuery(
        origin=origin,
        destination=destination,
        departure_date=departure_date,
        passengers=passengers,
    )
    offers = await flight_service.search_flights(query)
    return ApiResponse(
        success=True,
        message=f"Found {len(offers)} flight offers.",
        data=offers,
    )


@router.get(
    "/status/{flight_number}",
    response_model=ApiResponse[FlightStatus],
    summary="Get real-time flight status and disruption indicators",
)
async def get_flight_status(flight_number: str) -> ApiResponse[FlightStatus]:
    """Check live flight delay, departure gate, terminal, and disruption risk."""
    flight_stat = await flight_service.get_flight_status(flight_number)
    return ApiResponse(
        success=True,
        message="Flight status retrieved.",
        data=flight_stat,
    )
