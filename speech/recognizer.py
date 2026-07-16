"""
Project F.R.I.D.A.Y.
Speech Recognizer
"""

from __future__ import annotations

import numpy as np

from faster_whisper import WhisperModel

from speech.exceptions import (
    ModelNotLoadedError,
)

from speech.models import (
    TranscriptionResult,
)


class SpeechRecognizer:
    """
    Responsible for converting audio into text.
    """

    def __init__(self) -> None:

        self._model: WhisperModel | None = None

        self._model_name = "base"

    @property
    def model_loaded(self) -> bool:
        """
        Returns True if a speech model is loaded.
        """

        return self._model is not None

    def load_model(self) -> None:
        """
        Load the speech recognition model.
        """

        self._model = WhisperModel(
            self._model_name,
            device="cpu",
            compute_type="int8",
        )

    def unload_model(self) -> None:
        """
        Release the speech recognition model.
        """

        self._model = None

    def transcribe(
        self,
        audio: np.ndarray,
    ) -> TranscriptionResult:
        """
        Convert audio into text.
        """

        if self._model is None:
            raise ModelNotLoadedError(
                "Speech recognition model has not been loaded."
            )

        # Ensure Whisper receives a 1D float32 array.
        audio = np.asarray(audio, dtype=np.float32)

        if audio.ndim > 1:
            audio = audio.squeeze()

        segments, info = self._model.transcribe(
            audio,
            beam_size=5,
            language="en",
        )

        # Consume the generator so we can inspect/debug it.
        segments = list(segments)

        text = " ".join(
            segment.text.strip()
            for segment in segments
        ).strip()

        return TranscriptionResult(
            text=text,
            language=info.language,
            confidence=info.language_probability,
        )