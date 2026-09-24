from typing import Any


def search_flights(
    origin: str,
    destination: str,
) -> list[dict[str, Any]]:
    """
    Search available flights between two airports.

    This is currently mock data.
    Later this tool will call the Duffel integration.
    """

    flights = [
        {
            "flight_number": "AI101",
            "origin": "AMD",
            "destination": "DEL",
            "departure": "08:00",
            "arrival": "09:30",
            "price": 6500,
            "stops": 0,
        },
        {
            "flight_number": "AI205",
            "origin": "AMD",
            "destination": "DEL",
            "departure": "11:00",
            "arrival": "12:30",
            "price": 5200,
            "stops": 0,
        },
        {
            "flight_number": "6E312",
            "origin": "AMD",
            "destination": "DEL",
            "departure": "15:00",
            "arrival": "16:40",
            "price": 4800,
            "stops": 0,
        },
    ]

    return [
        flight
        for flight in flights
        if flight["origin"] == origin
        and flight["destination"] == destination
    ]