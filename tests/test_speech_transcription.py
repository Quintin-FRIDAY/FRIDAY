import time

from audio.audio_manager import AudioManager
from speech.recognizer import SpeechRecognizer


def main():

    audio = AudioManager()

    recognizer = SpeechRecognizer()

    recognizer.load_model()

    recorder = audio.get_recorder()

    print("Speak for 5 seconds...")

    recorder.start()

    time.sleep(5)

    recorder.stop()

    recording = recorder.get_audio()

    print(f"Shape: {recording.shape}")
    print(f"Samples: {recording.size}")
    print(f"Max amplitude: {recording.max():.3f}")
    print(f"Min amplitude: {recording.min():.3f}")

    recorder.save(
        "recordings/debug/whisper_test.wav"
    )

    result = recognizer.transcribe(recording)

    print("\n========== RESULT ==========\n")

    print(result.text)

    print("\nLanguage:", result.language)

    print("Confidence:", result.confidence)


if __name__ == "__main__":
    main()