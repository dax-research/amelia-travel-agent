"""Safety alert and push notification dispatch tools for LangChain agent."""

import json
from langchain_core.tools import tool


@tool
def send_guardian_alert(user_id: str, title: str, message: str, priority: str = "warning") -> str:
    """Send an immediate safety alert or flight disruption notification to the traveler's mobile device."""
    alert_status = {
        "status": "dispatched",
        "user_id": user_id,
        "title": title,
        "priority": priority,
        "message": message,
    }
    return json.dumps(alert_status)
