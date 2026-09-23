"""Local activity and attractions recommendation tools for LangChain agent."""

import json
from langchain_core.tools import tool


@tool
def recommend_activities(destination: str, interest_category: str) -> str:
    """Recommend points of interest, tours, and culinary experiences in a destination based on traveler interests."""
    recommendations = [
        {
            "title": f"Historic Walking Tour of {destination.title()}",
            "category": "culture",
            "duration_hours": 2.5,
            "cost_usd": 30.0,
            "highlight": "Explore hidden courtyards and architectural heritage.",
        },
        {
            "title": f"Sunset Culinary & Wine Tasting in {destination.title()}",
            "category": "dining",
            "duration_hours": 3.0,
            "cost_usd": 65.0,
            "highlight": "Sample 5 local delicacies with sommelier pairings.",
        },
    ]
    return json.dumps(recommendations)
