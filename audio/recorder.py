"""
Audio recording subsystem.

This module contains the AudioRecorder class responsible for managing
microphone recording state and audio buffering.

Actual recording functionality is implemented incrementally throughout
Phase 3.1.
"""

from __future__ import annotations

import threading
from core.logger import log

import numpy as np

import wave

from audio.streams import InputAudioStream

from core.models.audio_configuration import AudioConfiguration

from audio.exceptions import (RecordingAlreadyRunningError, RecordingNotRunningError,)

from pathlib import Path

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

        # Active input stream
        self._stream: InputAudioStream | None = None

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
            self._stream = InputAudioStream(configuration=self._configuration, callback=self._audio_callback,)
            self._stream.start()

            
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

            if self._stream is not None:
                self._stream.stop()
                self._stream.close()
                self._stream = None

    def cancel(self) -> None:
        """
        Cancel the recording and discard buffered audio.
        """

        with self._lock:
            self._frames.clear()
            self._recording = False

        if self._stream is not None:
            self._stream.stop()
            self._stream.close()
            self._stream = None

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
        
    def save(self, path: str | Path) -> None:
        """
        Save the recorded audio to a WAV file.
        """

        path = Path(path)

        path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        audio = self.get_audio()

        if audio.size == 0:
            raise ValueError("No recorded audio to save.")

        pcm = np.clip(audio, -1.0, 1.0)

        pcm = (pcm * 32767).astype(np.int16)

        with wave.open(str(path), "wb") as wav:

            wav.setnchannels(self._configuration.channels)

            wav.setsampwidth(2)

            wav.setframerate(
                self._configuration.sample_rate
            )

            wav.writeframes(pcm.tobytes())
    
    def _audio_callback(self, indata: np.ndarray, frames: int, time, status,) -> None:
        """
        Receive microphone audio from the input stream.
        """

        if status:
            log(
                f"Audio stream status: {status}",
                level="WARNING",
            )
            

        with self._lock:
            if self._recording:
                self._frames.append(indata.copy())