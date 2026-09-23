"""Flight lookup and status tools for LangChain agent."""

import json
from langchain_core.tools import tool


@tool
def search_flights(origin: str, destination: str, departure_date: str) -> str:
    """Search for flight options between origin and destination airport codes on a specific date (YYYY-MM-DD)."""
    offers = [
        {
            "flight_id": f"FL_{origin.upper()}_{destination.upper()}_101",
            "airline": "Skyward Global",
            "origin": origin.upper(),
            "destination": destination.upper(),
            "departure_time": f"{departure_date} 08:30",
            "arrival_time": f"{departure_date} 11:45",
            "price_usd": 380.0,
            "non_stop": True,
        },
        {
            "flight_id": f"FL_{origin.upper()}_{destination.upper()}_204",
            "airline": "AeroWings",
            "origin": origin.upper(),
            "destination": destination.upper(),
            "departure_time": f"{departure_date} 14:00",
            "arrival_time": f"{departure_date} 17:15",
            "price_usd": 320.0,
            "non_stop": True,
        },
    ]
    return json.dumps(offers)


@tool
def check_flight_status(flight_number: str) -> str:
    """Check real-time flight status, delay information, and terminal gate for a flight number."""
    status = {
        "flight_number": flight_number.upper(),
        "status": "on_time",
        "delay_minutes": 0,
        "terminal": "T2",
        "gate": "B22",
        "advisory": "Flight operating on schedule.",
    }
    return json.dumps(status)
