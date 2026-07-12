"""
Project F.R.I.D.A.Y.
Audio Configuration Model
"""

from __future__ import annotations

from dataclasses import dataclass

from core.models.audio_device import AudioDevice


@dataclass(slots=True)
class AudioConfiguration:
    """
    Represents the active audio configuration.
    """

    sample_rate: int = 16000
    channels: int = 1
    dtype: str = "float32"

    input_device: AudioDevice | None = None
    output_device: AudioDevice | None = None

    block_size: int = 1024