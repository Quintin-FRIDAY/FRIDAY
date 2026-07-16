from audio.audio_manager import AudioManager
from voice.pipeline import VoicePipeline

audio = AudioManager()
pipeline = VoicePipeline(audio)

# Force an empty recording
pipeline._recorder.clear()

recording = pipeline._recorder.get_audio()

print(recording.size)