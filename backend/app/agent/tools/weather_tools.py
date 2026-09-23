"""Weather monitoring and storm advisory tools for LangChain agent."""

import json
from langchain_core.tools import tool


@tool
def get_weather_forecast(city: str) -> str:
    """Fetch current temperature, conditions, and travel weather warnings for a destination."""
    forecast = {
        "city": city.title(),
        "temperature_c": 22.0,
        "condition": "Clear and Sunny",
        "advisory": "Optimal weather for outdoor exploration.",
        "severe_alert": False,
    }
    return json.dumps(forecast)
