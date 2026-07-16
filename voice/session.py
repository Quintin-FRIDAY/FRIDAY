"""
Project F.R.I.D.A.Y.
Voice Session
"""

from __future__ import annotations

from speech.models import TranscriptionResult

from voice.pipeline import VoicePipeline


class VoiceSession:
    """
    Represents a single voice interaction.
    """

    def __init__(
        self,
        pipeline: VoicePipeline,
    ) -> None:

        self._pipeline = pipeline

    def listen(
        self,
        duration: float = 5.0,
    ) -> TranscriptionResult:
        """
        Listen for a single spoken request.
        """

        return self._pipeline.listen(duration)