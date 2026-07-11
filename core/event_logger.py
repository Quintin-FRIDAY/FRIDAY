"""
Project F.R.I.D.A.Y.
Event Logger
"""

from core.events import event_bus


def log_event(event):
    print(f"[EVENT] {event.name} -> {event.data}")


event_bus.subscribe("assistant_started", log_event)
event_bus.subscribe("assistant_stopped", log_event)
event_bus.subscribe("plugin_loaded", log_event)
event_bus.subscribe("plugin_failed", log_event)
event_bus.subscribe("command_received", log_event)
event_bus.subscribe("command_handled", log_event)
event_bus.subscribe("command_unhandled", log_event)
event_bus.subscribe("user_command", log_event)
event_bus.subscribe("assistant_response", log_event)