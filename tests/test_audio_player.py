from audio.player import AudioPlayer
from core.models.audio_configuration import AudioConfiguration


def main():

    player = AudioPlayer(AudioConfiguration())

    print("AudioPlayer created successfully.")
    print(f"Playing: {player.is_playing}")


if __name__ == "__main__":
    main()