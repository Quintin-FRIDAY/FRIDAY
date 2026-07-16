from audio.audio_manager import AudioManager

from voice.pipeline import VoicePipeline
from voice.session import VoiceSession


def main():

    audio = AudioManager()

    pipeline = VoicePipeline(audio)

    session = VoiceSession(pipeline)

    print("Speak for 5 seconds...")

    result = session.listen()

    print("\n========== RESULT ==========\n")

    print(result.text)


if __name__ == "__main__":
    main()