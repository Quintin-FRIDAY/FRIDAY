"""
Project F.R.I.D.A.Y.
Audio Manager
"""

from core.models.audio_device import AudioDevice
from core.models.audio_configuration import AudioConfiguration

from audio.player import AudioPlayer
from audio.recorder import AudioRecorder

from audio.devices import (
    get_all_devices,
    get_input_devices,
    get_output_devices,
)


class AudioManager:
    """
    Responsible for managing all audio functionality.
    """

    def __init__(self):

        input_devices = get_input_devices()
        output_devices = get_output_devices()

        self.input_device: AudioDevice | None = (
            input_devices[0] if input_devices else None
        )

        self.output_device: AudioDevice | None = (
            output_devices[0] if output_devices else None
        )

        self.configuration = AudioConfiguration()

        self.recorder = AudioRecorder(
            self.configuration
        )

        self.player = AudioPlayer(
            self.configuration
        )

    # --------------------------------------------------
    # Device Lists
    # --------------------------------------------------

    def get_devices(self) -> list[AudioDevice]:
        """
        Return every detected audio device.
        """

        return get_all_devices()

    def get_input_devices(self) -> list[AudioDevice]:
        """
        Return every microphone.
        """

        return get_input_devices()

    def get_output_devices(self) -> list[AudioDevice]:
        """
        Return every speaker.
        """

        return get_output_devices()

    # --------------------------------------------------
    # Active Devices
    # --------------------------------------------------

    def get_input_device(self) -> AudioDevice | None:
        """
        Return the selected microphone.
        """

        return self.input_device

    def get_output_device(self) -> AudioDevice | None:
        """
        Return the selected speaker.
        """

        return self.output_device

    def set_input_device(self, device: AudioDevice):
        """
        Select a microphone.
        """

        self.input_device = device

    def set_output_device(self, device: AudioDevice):
        """
        Select a speaker.
        """

        self.output_device = device

    # --------------------------------------------------
    # Configuration
    # --------------------------------------------------

    def get_configuration(self) -> AudioConfiguration:
        """
        Return the current audio configuration.
        """

        return self.configuration


    def set_configuration(
        self,
        configuration: AudioConfiguration
    ):
        """
        Replace the current audio configuration.
        """

        self.configuration = configuration

    # --------------------------------------------------
    # Audio Components
    # --------------------------------------------------

    def get_recorder(self) -> AudioRecorder:
        """
        Return the audio recorder.
        """

        return self.recorder


    def get_player(self) -> AudioPlayer:
        """
        Return the audio player.
        """

        return self.player