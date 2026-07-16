from audio.audio_manager import AudioManager


class Audio:
    """Provides access to audio configuration."""

    def __init__(self):
        self.audio = AudioManager()

    def current(self):
        return {
            "input": self.audio.input_device,
            "output": self.audio.output_device,
            "configuration": self.audio.configuration,
        }
    
    def set_input(self, index: int):

        devices = self.audio.get_input_devices()

        for device in devices:
            if device.id == index:
                self.audio.set_input_device(device)
                return device

        return None


    def set_output(self, index: int):

        devices = self.audio.get_output_devices()

        for device in devices:
            if device.id == index:
                self.audio.set_output_device(device)
                return device

        return None
    
    def input_devices(self):
        """
        Return all available input devices.
        """
        return self.audio.get_input_devices()


    def output_devices(self):
        """
        Return all available output devices.
        """
        return self.audio.get_output_devices()


    def set_input(self, index: int):
        """
        Set the active input device.
        """

        for device in self.input_devices():
            if device.id == index:
                self.audio.set_input_device(device)
                return device

        return None


    def set_output(self, index: int):
        """
        Set the active output device.
        """

        for device in self.output_devices():
            if device.id == index:
                self.audio.set_output_device(device)
                return device

        return None