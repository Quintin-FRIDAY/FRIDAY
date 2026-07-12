from audio.streams import InputAudioStream
from core.models.audio_configuration import AudioConfiguration

config = AudioConfiguration()

stream = InputAudioStream(
    configuration=config,
    callback=lambda *args: None,
)

print("Stream created successfully.")