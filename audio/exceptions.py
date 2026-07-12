"""
Project F.R.I.D.A.Y.
Audio Exceptions
"""


class AudioError(Exception):
    """Base exception for the audio subsystem."""


class RecordingAlreadyRunningError(AudioError):
    """Raised when attempting to start an active recording."""


class RecordingNotRunningError(AudioError):
    """Raised when attempting to stop a recording that isn't running."""