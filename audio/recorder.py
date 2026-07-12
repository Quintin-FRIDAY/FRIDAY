"""
Audio recording subsystem.

This module contains the AudioRecorder class responsible for managing
microphone recording state and audio buffering.

Actual recording functionality is implemented incrementally throughout
Phase 3.1.
"""

from __future__ import annotations

import threading
from typing import Optional

import numpy as np

from core.models.audio_configuration import AudioConfiguration

from audio.exceptions import (RecordingAlreadyRunningError, RecordingNotRunningError,)

class AudioRecorder:
    """
    Handles microphone recording.

    This class is responsible only for recording audio.

    It does NOT:

    - detect audio devices
    - manage configuration
    - perform speech recognition
    - perform wake-word detection

    Those responsibilities belong to other components.
    """

    def __init__(self, configuration: AudioConfiguration) -> None:
        """
        Initialize the recorder.

        Args:
            configuration:
                Audio recording configuration.
        """

        self._configuration = configuration

        # Input stream (created later)
        self._stream: Optional[object] = None

        # Buffered audio chunks
        self._frames: list[np.ndarray] = []

        # Recording state
        self._recording = False

        # Protect shared resources
        self._lock = threading.Lock()

    @property
    def configuration(self) -> AudioConfiguration:
        """
        Return the active audio configuration.
        """
        return self._configuration

    @property
    def is_recording(self) -> bool:
        """
        Returns True while actively recording.
        """
        return self._recording
    
    def start(self) -> None:
        """
        Begin a recording session.
        """

        with self._lock:

            if self._recording:
                raise RecordingAlreadyRunningError(
                    "Recording is already in progress."
                )

            self._frames.clear()
            self._recording = True

    def stop(self) -> None:
        """
        Stop the active recording session.
        """

        with self._lock:

            if not self._recording:
                raise RecordingNotRunningError(
                    "No recording is currently in progress."
                )

            self._recording = False

    def cancel(self) -> None:
        """
        Cancel the recording and discard buffered audio.
        """

        with self._lock:
            self._frames.clear()
            self._recording = False

    def clear(self) -> None:
        """
        Remove any buffered audio.
        """

        with self._lock:
            self._frames.clear()

    def get_audio(self) -> np.ndarray:
        """
        Return the recorded audio.
        """

        with self._lock:

            if not self._frames:
                return np.array([], dtype=np.float32)

            return np.concatenate(self._frames)
        
    def save(self, path: str) -> None:
        """
        Save recorded audio.

        Implemented in a later step.
        """

        raise NotImplementedError(
            "Audio saving has not been implemented yet."
        )