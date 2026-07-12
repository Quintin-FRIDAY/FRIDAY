import time
from pathlib import Path

from audio.player import AudioPlayer
from audio.recorder import AudioRecorder
from core.models.audio_configuration import AudioConfiguration

recorder = AudioRecorder(AudioConfiguration())
for i in range(3):

    recorder.start()

    time.sleep(2)

    recorder.stop()

    recorder.save(
        f"recordings/debug/test_{i}.wav"
    )