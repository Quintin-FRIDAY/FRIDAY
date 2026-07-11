"""
Project F.R.I.D.A.Y.
Audio Test
"""

from audio.audio_manager import AudioManager


def main():

    audio = AudioManager()

    print("\n========== INPUT DEVICES ==========\n")

    inputs = audio.get_input_devices()

    for device in inputs:

        default = " (Default)" if device.is_default_input else ""

        print(
            f"[{device.id}] "
            f"{device.name}"
            f"{default}"
        )

    print("\n========== OUTPUT DEVICES ==========\n")

    outputs = audio.get_output_devices()

    for device in outputs:

        default = " (Default)" if device.is_default_output else ""

        print(
            f"[{device.id}] "
            f"{device.name}"
            f"{default}"
        )

    print("\n========== CURRENT DEVICES ==========\n")

    if audio.get_input_device():
        print(
            f"Input : {audio.get_input_device().name}"
        )

    if audio.get_output_device():
        print(
            f"Output: {audio.get_output_device().name}"
        )

    # Example of changing devices

    if len(inputs) > 1:
        audio.set_input_device(inputs[1])

    if len(outputs) > 1:
        audio.set_output_device(outputs[1])

    print("\n========== AFTER CHANGE ==========\n")

    if audio.get_input_device():
        print(
            f"Input : {audio.get_input_device().name}"
        )

    if audio.get_output_device():
        print(
            f"Output: {audio.get_output_device().name}"
        )


if __name__ == "__main__":
    main()