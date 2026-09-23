"""Smart Guardian notifications and travel alert endpoints."""

from typing import List
from fastapi import APIRouter, Depends, status
from app.core.dependencies import get_current_user_id
from app.schemas.common import ApiResponse
from app.schemas.notification import NotificationCreate, NotificationResponse
from app.services.notification_service import notification_service

router = APIRouter(prefix="/notifications", tags=["Notifications"])


@router.post(
    "",
    response_model=ApiResponse[NotificationResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Dispatch a safety or disruption notification",
)
async def dispatch_notification(
    payload: NotificationCreate,
) -> ApiResponse[NotificationResponse]:
    """Send alert through configured channels (push, SMS, in-app)."""
    notification = await notification_service.send_notification(payload)
    return ApiResponse(
        success=True,
        message="Notification dispatched successfully.",
        data=notification,
    )


@router.get(
    "",
    response_model=ApiResponse[List[NotificationResponse]],
    summary="List notifications for authenticated user",
)
async def list_my_notifications(
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[List[NotificationResponse]]:
    """Retrieve traveler's guardian alerts and advisory history."""
    notifications = notification_service.list_user_notifications(user_id=user_id)
    return ApiResponse(
        success=True,
        message=f"Retrieved {len(notifications)} notifications.",
        data=notifications,
    )
