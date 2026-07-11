"""
Project F.R.I.D.A.Y.
Event Logger
"""

from core.events import event_bus
from core.models.event_type import EventType

def log_event(event):
    print(f"[EVENT] {event.name} -> {event.data}")


event_bus.subscribe(EventType.ASSISTANT_STARTED, log_event)
event_bus.subscribe(EventType.ASSISTANT_STOPPED, log_event)
event_bus.subscribe(EventType.PLUGIN_LOADED, log_event)
event_bus.subscribe(EventType.PLUGIN_FAILED, log_event)
event_bus.subscribe(EventType.COMMAND_RECEIVED, log_event)
event_bus.subscribe(EventType.COMMAND_HANDLED, log_event)
event_bus.subscribe(EventType.COMMAND_UNHANDLED, log_event)
event_bus.subscribe(EventType.USER_COMMAND, log_event)
event_bus.subscribe(EventType.ASSISTANT_RESPONSE, log_event)