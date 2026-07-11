"""
Project F.R.I.D.A.Y.
Event Types
"""

from enum import StrEnum


class EventType(StrEnum):
    """
    All event names used throughout F.R.I.D.A.Y.
    """

    # Assistant
    ASSISTANT_STARTED = "assistant_started"
    ASSISTANT_STOPPED = "assistant_stopped"
    ASSISTANT_INTRODUCED = "assistant_introduced"

    # User
    USER_COMMAND = "user_command"

    # AI
    ASSISTANT_RESPONSE = "assistant_response"

    # Command Processing
    COMMAND_RECEIVED = "command_received"
    COMMAND_HANDLED = "command_handled"
    COMMAND_UNHANDLED = "command_unhandled"

    # Plugins
    PLUGIN_LOADED = "plugin_loaded"
    PLUGIN_FAILED = "plugin_failed"

    # Services
    SERVICE_STARTED = "service_started"
    SERVICE_STOPPED = "service_stopped"
    SERVICE_FAILED = "service_failed"

    # Memory
    MEMORY_SAVED = "memory_saved"
    MEMORY_LOADED = "memory_loaded"

    # Settings
    SETTINGS_LOADED = "settings_loaded"
    SETTINGS_SAVED = "settings_saved"