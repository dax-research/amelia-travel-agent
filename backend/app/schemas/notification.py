"""Pydantic schemas for guardian safety notifications and flight disruption alerts."""

from datetime import datetime
from enum import Enum
from typing import Any, Dict, Optional
from pydantic import BaseModel, Field


class NotificationPriority(str, Enum):
    """Urgency level of the alert."""

    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class NotificationChannel(str, Enum):
    """Delivery transport for notification."""

    PUSH = "push"
    SMS = "sms"
    EMAIL = "email"
    IN_APP = "in_app"


class NotificationCreate(BaseModel):
    """Payload to dispatch a notification to a traveler."""

    user_id: str
    title: str
    message: str
    priority: NotificationPriority = NotificationPriority.INFO
    channel: NotificationChannel = NotificationChannel.IN_APP
    trip_id: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)


class NotificationResponse(BaseModel):
    """Notification record returned to the client."""

    id: str
    user_id: str
    title: str
    message: str
    priority: NotificationPriority
    channel: NotificationChannel
    is_read: bool = False
    created_at: datetime
