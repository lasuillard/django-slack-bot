"""Dummy backend doing nothing."""
from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING, Any

from .base import BackendBase

if TYPE_CHECKING:
    from slack_sdk.web import SlackResponse

logger = getLogger(__name__)


class DummyBackend(BackendBase):
    """An dummy backend that does nothing with message."""

    def send_message(self, *args: Any, **kwargs: Any) -> None:
        """This backend will not do anything, just like dummy."""

    def _send_message(self, *args: Any, **kwargs: Any) -> SlackResponse | None:
        ...

    def _record_request(self, *args: Any, **kwargs: Any) -> Any:
        ...

    def _record_response(self, *args: Any, **kwargs: Any) -> Any:
        ...