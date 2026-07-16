"""
Project F.R.I.D.A.Y.
Voice Exceptions
"""


class VoicePipelineError(Exception):
    """
    Base exception for all voice pipeline errors.
    """


class NoSpeechDetectedError(VoicePipelineError):
    """
    Raised when no speech is detected.
    """


class VoiceTimeoutError(VoicePipelineError):
    """
    Raised when recording exceeds the allowed duration.
    """


class EmptyRecordingError(VoicePipelineError):
    """
    Raised when no audio was recorded.
    """


class SpeechRecognitionFailedError(VoicePipelineError):
    """
    Raised when speech recognition fails.
    """