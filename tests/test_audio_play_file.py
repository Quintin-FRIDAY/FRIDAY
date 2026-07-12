from pathlib import Path

from audio.player import AudioPlayer
from core.models.audio_configuration import AudioConfiguration


def main():

    player = AudioPlayer(AudioConfiguration())

    recording = Path(
        "recordings/debug/test.wav"
    )

    print("Playing WAV file...")

    player.play_file(recording)

    print("Done.")


if __name__ == "__main__":
    main()