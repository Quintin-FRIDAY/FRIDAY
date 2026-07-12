import time

from audio.audio_manager import AudioManager


def main():

    audio = AudioManager()

    recorder = audio.get_recorder()
    player = audio.get_player()

    print("Recording...")

    recorder.start()

    time.sleep(5)

    recorder.stop()

    recording = recorder.get_audio()

    print("Playing...")

    player.play(recording)

    print("Finished.")
    
    print(
        recorder.configuration is player.configuration
    )


if __name__ == "__main__":
    main()

    