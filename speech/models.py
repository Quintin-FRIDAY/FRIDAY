"""
Project F.R.I.D.A.Y.
Speech Recognition Models
"""

from dataclasses import dataclass


@dataclass(slots=True)
class TranscriptionResult:
    """
    Represents the result of a speech transcription.
    """

    text: str
    language: str
    confidence: float