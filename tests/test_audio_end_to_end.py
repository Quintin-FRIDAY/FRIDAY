import time
from pathlib import Path

from audio.audio_manager import AudioManager


def main():

    audio = AudioManager()

    inputs = audio.get_input_devices()

    print("Available microphones:\n")

    for index, device in enumerate(inputs):
        print(f"{index}: {device.name} ({device.host_api})")

    # Select the microphone you want to test
    audio.set_input_device(inputs[2])

    print(f"\nSelected microphone: {audio.get_input_device().name}")

    recorder = audio.get_recorder()

    print("\nRecording for 5 seconds...")

    recorder.start()

    time.sleep(5)

    recorder.stop()

    output = Path("recordings/debug/device_test.wav")

    recorder.save(output)

    print(f"\nRecording saved to: {output}")


if __name__ == "__main__":
    main()