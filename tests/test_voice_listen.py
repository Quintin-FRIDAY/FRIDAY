from audio.audio_manager import AudioManager
from voice.pipeline import VoicePipeline


def main():

    audio = AudioManager()

    pipeline = VoicePipeline(audio)

    print("Speak for 5 seconds...")

    result = pipeline.listen()

    print("\n========== RESULT ==========\n")

    print(result.text)

    print(f"\nLanguage: {result.language}")

    print(f"Confidence: {result.confidence}")


if __name__ == "__main__":
    main()