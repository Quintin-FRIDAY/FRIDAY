"""
Project F.R.I.D.A.Y.
Audio Player
"""

from __future__ import annotations

import threading
from pathlib import Path

import numpy as np

import wave

from audio.streams import OutputAudioStream

from core.models.audio_configuration import AudioConfiguration


class AudioPlayer:
    """
    Handles audio playback.

    This class is responsible for playing audio through the
    selected output device.
    """

    def __init__(
        self,
        configuration: AudioConfiguration,
    ) -> None:

        self._configuration = configuration

        self._stream = OutputAudioStream(
            configuration,
        )

        self._playing = False

        self._lock = threading.Lock()

    @property
    def configuration(self) -> AudioConfiguration:
        """
        Return the active audio configuration.
        """
        return self._configuration

    @property
    def is_playing(self) -> bool:
        """
        Returns True while audio is playing.
        """
        return self._playing
    
    def play(self, audio: np.ndarray) -> None:
        """
        Play audio from a NumPy array.
        """
        with self._lock:

            self._playing = True

        self._stream.play(audio)

        self._stream.wait()

        with self._lock:

            self._playing = False


    def play_file(self,path: str | Path) -> None:
        """
        Play a WAV file.
        """

        path = Path(path)

        with wave.open(str(path), "rb") as wav:

            frames = wav.readframes(wav.getnframes())

            audio = np.frombuffer(
                frames,
                dtype=np.int16,
            )

            if wav.getnchannels() > 1:
                audio = audio.reshape(
                    -1,
                    wav.getnchannels(),
                )

            audio = audio.astype(np.float32) / 32767.0

        self.play(audio)


    def stop(self) -> None:
        """
        Stop playback.
        """
        with self._lock:

            self._stream.stop()

            self._playing = False