import time

from audio.player import AudioPlayer
from audio.recorder import AudioRecorder
from core.models.audio_configuration import AudioConfiguration


config = AudioConfiguration()

recorder = AudioRecorder(config)
player = AudioPlayer(config)

print("Recording...")

recorder.start()

time.sleep(5)

recorder.stop()

audio = recorder.get_audio()

print("Playing...")

player.play(audio)

print("Done.")