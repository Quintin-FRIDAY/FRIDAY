"""
Project F.R.I.D.A.Y.
Event Bus
"""

from collections import defaultdict
from typing import Callable

from core.models.event import Event


class EventBus:
    """
    Central event dispatcher.
    """

    def __init__(self):
        self.listeners: dict[str, list[Callable]] = defaultdict(list)

    def subscribe(self, event_name: str, callback: Callable):
        """
        Subscribe to an event.
        """

        self.listeners[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: Callable):
        """
        Remove a listener.
        """

        if callback in self.listeners[event_name]:
            self.listeners[event_name].remove(callback)

    def emit(self, event_name: str, **data):
        """
        Emit an event.
        """

        event = Event(
            name=event_name,
            data=data
        )

        for callback in self.listeners[event_name]:
            callback(event)