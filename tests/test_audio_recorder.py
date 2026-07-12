import time

from audio.recorder import AudioRecorder
from core.models.audio_configuration import AudioConfiguration
from pathlib import Path

recorder = AudioRecorder(AudioConfiguration())

print("Recording...")

recorder.start()

time.sleep(5)

recorder.stop()

recording = Path(
    "recordings/debug/test.wav"
)

recorder.save(recording)

print("Saved!")