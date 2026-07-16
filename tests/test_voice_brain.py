from audio.audio_manager import AudioManager

from core.brain import Brain

from voice.pipeline import VoicePipeline
from voice.session import VoiceSession
from voice.controller import VoiceController


audio = AudioManager()

pipeline = VoicePipeline(audio)

session = VoiceSession(pipeline)

brain = Brain()

controller = VoiceController(
    session,
    brain,
)


response = controller.process_once()

print(response)