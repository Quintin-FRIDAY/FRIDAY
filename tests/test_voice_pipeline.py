from audio.audio_manager import AudioManager

from voice.pipeline import VoicePipeline


def main():

    audio = AudioManager()

    pipeline = VoicePipeline(audio)

    print("Voice pipeline created successfully.")


if __name__ == "__main__":
    main()