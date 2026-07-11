"""
Project F.R.I.D.A.Y.
Audio Device Utilities
"""

import sounddevice as sd

from core.models.audio_device import AudioDevice


def get_all_devices() -> list[AudioDevice]:
    """
    Return every available audio device.
    """

    devices = []

    default_input, default_output = sd.default.device
    host_apis = sd.query_hostapis()

    for index, device in enumerate(sd.query_devices()):

        host_api_name = host_apis[device["hostapi"]]["name"]

        devices.append(

            AudioDevice(
                id=index,
                name=device["name"],

                host_api=host_api_name,

                default_samplerate=device["default_samplerate"],

                max_input_channels=device["max_input_channels"],
                max_output_channels=device["max_output_channels"],

                is_default_input=index == default_input,
                is_default_output=index == default_output,

                is_input=device["max_input_channels"] > 0,
                is_output=device["max_output_channels"] > 0
            )

        )

    return devices


def get_input_devices() -> list[AudioDevice]:
    """
    Return every microphone.
    """

    return [
        device
        for device in get_all_devices()
        if device.is_input
    ]


def get_output_devices() -> list[AudioDevice]:
    """
    Return every speaker.
    """

    return [
        device
        for device in get_all_devices()
        if device.is_output
    ]