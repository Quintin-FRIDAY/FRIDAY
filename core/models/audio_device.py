"""
Project F.R.I.D.A.Y.
Audio Device Model
"""

from dataclasses import dataclass


@dataclass
class AudioDevice:
    """
    Represents an audio device.
    """

    id: int
    name: str

    host_api: str

    default_samplerate: float

    max_input_channels: int
    max_output_channels: int

    is_default_input: bool
    is_default_output: bool

    is_input: bool
    is_output: bool