"""
Project F.R.I.D.A.Y.
Audio Streams
"""

from __future__ import annotations

from typing import Callable

import numpy as np
import sounddevice as sd

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
            device=(
                self._configuration.input_device.id
                if self._configuration.input_device
                else None
            ),
            samplerate=self._configuration.sample_rate,
            channels=self._configuration.channels,
            dtype=self._configuration.dtype,
            blocksize=self._configuration.block_size,
            callback=callback,
        )

    def start(self) -> None:
        """
        Start the audio stream.
        """
        self._stream.start()

    def stop(self) -> None:
        """
        Stop the audio stream.
        """
        self._stream.stop()

    def close(self) -> None:
        """
        Close the audio stream.
        """
        self._stream.close()

    @property
    def active(self) -> bool:
        """
        Return whether the stream is active.
        """
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

    def play(
        self,
        audio: np.ndarray,
    ) -> None:
        """
        Play a NumPy audio buffer.
        """

        sd.play(
            audio,
            samplerate=self._configuration.sample_rate,
            device=(
                self._configuration.output_device.id
                if self._configuration.output_device
                else None
            ),
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