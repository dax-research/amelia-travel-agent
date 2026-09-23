"""Unit tests for LangChain agent tools."""

import json
from app.agent.tools.flight_tools import search_flights, check_flight_status
from app.agent.tools.hotel_tools import search_hotels
from app.agent.tools.booking_tools import book_travel_item
from app.agent.tools.weather_tools import get_weather_forecast


def test_flight_tools():
    """Verify search_flights and check_flight_status tool executions."""
    flights_json = search_flights.invoke({"origin": "JFK", "destination": "CDG", "departure_date": "2026-10-15"})
    flights = json.loads(flights_json)
    assert isinstance(flights, list)
    assert len(flights) > 0

    status_json = check_flight_status.invoke({"flight_number": "SK101"})
    status = json.loads(status_json)
    assert status["flight_number"] == "SK101"
    assert "status" in status


def test_hotel_and_weather_tools():
    """Verify hotel search and weather tool executions."""
    hotels_json = search_hotels.invoke({"city": "Vienna", "check_in": "2026-11-01", "check_out": "2026-11-05"})
    hotels = json.loads(hotels_json)
    assert len(hotels) > 0

    weather_json = get_weather_forecast.invoke({"city": "Vienna"})
    weather = json.loads(weather_json)
    assert "temperature_c" in weather
    assert weather["city"] == "Vienna"


def test_booking_tool():
    """Verify booking tool confirmation code generation."""
    booking_json = book_travel_item.invoke({
        "booking_type": "flight",
        "item_id": "FL_101",
        "traveler_name": "Test Traveler",
    })
    booking = json.loads(booking_json)
    assert booking["status"] == "confirmed"
    assert "booking_reference" in booking
