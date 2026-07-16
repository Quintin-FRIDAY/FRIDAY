import time

from audio.audio_manager import AudioManager


def main():

    audio = AudioManager()

    recorder = audio.get_recorder()
    recognizer = audio.get_speech_recognizer()

    print("Speak for 5 seconds...")

    recorder.start()

    time.sleep(5)

    recorder.stop()

    recording = recorder.get_audio()

    result = recognizer.transcribe(recording)

    print("\n========== RESULT ==========\n")
    print(result.text)

    print(
        audio.get_speech_recognizer().model_loaded
    )

if __name__ == "__main__":
    main()   