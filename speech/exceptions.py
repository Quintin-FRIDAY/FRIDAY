"""
Project F.R.I.D.A.Y.
Speech Recognition Exceptions
"""


class SpeechRecognitionError(Exception):
    """
    Base exception for speech recognition.
    """


class ModelNotLoadedError(SpeechRecognitionError):
    """
    Raised when a recognition model has not been loaded.
    """


class TranscriptionError(SpeechRecognitionError):
    """
    Raised when transcription fails.
    """