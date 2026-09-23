"""Base external API integration client using httpx."""

import logging
from typing import Any, Dict, Optional
import httpx


class BaseIntegrationClient:
    """Base HTTP client for third-party travel APIs."""

    def __init__(self, base_url: str, api_key: Optional[str] = None, timeout: float = 10.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout = timeout
        self.logger = logging.getLogger(self.__class__.__name__)

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Perform an asynchronous GET request."""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        headers = self._get_headers()
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.get(url, params=params, headers=headers)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as err:
                self.logger.error("HTTP error %s requesting %s", err.response.status_code, url)
                raise
            except Exception as err:
                self.logger.error("Network or unexpected error requesting %s: %s", url, err)
                raise

    def _get_headers(self) -> Dict[str, str]:
        """Generate authorization and standard headers."""
        headers = {"User-Agent": "AITravelConcierge/0.1.0"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        return headers
