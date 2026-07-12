"""
Project F.R.I.D.A.Y.
Audio Player
"""

from __future__ import annotations

import threading
from pathlib import Path

import numpy as np

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

        self._stream = None

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
        raise NotImplementedError


    def play_file(self, path: str | Path) -> None:
        """
        Play audio from a WAV file.
        """
        raise NotImplementedError


    def stop(self) -> None:
        """
        Stop playback.
        """
        raise NotImplementedError