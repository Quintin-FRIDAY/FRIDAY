import time

from audio.recorder import AudioRecorder
from core.models.audio_configuration import AudioConfiguration


def main():

    recorder = AudioRecorder(AudioConfiguration())

    print("Recording for 5 seconds...")
    print("Speak into your microphone.\n")

    recorder.start()

    time.sleep(5)

    recorder.stop()

    audio = recorder.get_audio()

    print(f"Recording finished.")
    print(f"Shape   : {audio.shape}")
    print(f"Samples : {audio.size}")


if __name__ == "__main__":
    main()