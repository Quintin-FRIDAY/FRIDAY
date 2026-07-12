"""
Project F.R.I.D.A.Y.
Audio Streams
"""

from __future__ import annotations

from typing import Callable

import sounddevice as sd

import numpy as np

from core.models.audio_configuration import AudioConfiguration


class InputAudioStream:
    """
    Wraps a sounddevice.InputStream.

    This class isolates the rest of the application from the
    underlying audio backend.
    """

    def __init__(
        self,
        configuration: AudioConfiguration,
        callback: Callable,
    ) -> None:

        self._configuration = configuration

        self._stream = sd.InputStream(
            samplerate=configuration.sample_rate,
            channels=configuration.channels,
            dtype=configuration.dtype,
            blocksize=configuration.block_size,
            callback=callback,
        )

    def start(self) -> None:
        """Start the audio stream."""
        self._stream.start()

    def stop(self) -> None:
        """Stop the audio stream."""
        self._stream.stop()

    def close(self) -> None:
        """Close the audio stream."""
        self._stream.close()

    @property
    def active(self) -> bool:
        """Return whether the stream is active."""
        return self._stream.active
    
class OutputAudioStream:
    """
    Wraps audio playback through sounddevice.
    """

    def __init__(
        self,
        configuration: AudioConfiguration,
    ) -> None:

        self._configuration = configuration

    def play(self, audio: np.ndarray,) -> None:
        """
        Play a NumPy audio buffer.
        """

        sd.play(
            audio,
            samplerate=self._configuration.sample_rate,
        )

    def stop(self) -> None:
        """
        Stop playback.
        """

        sd.stop()

    def wait(self) -> None:
        """
        Wait until playback has completed.
        """

        sd.wait()