from audio.recorder import AudioRecorder
from core.models.audio_configuration import AudioConfiguration

config = AudioConfiguration()
recorder = AudioRecorder(config)

print("Initial:", recorder.is_recording)

recorder.start()
print("Started:", recorder.is_recording)

recorder.stop()
print("Stopped:", recorder.is_recording)

print("Audio:", recorder.get_audio())