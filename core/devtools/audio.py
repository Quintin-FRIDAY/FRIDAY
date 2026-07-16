from core.audio import Audio

audio = Audio()


def process_audio(command: str):

    if not command.startswith("/audio"):
        return None

    if command == "/audio current":

        current = audio.current()

        input_device = current["input"]
        output_device = current["output"]
        config = current["configuration"]

        return (
            "=== Current Audio Configuration ===\n\n"
            f"Input Device : {input_device.name if input_device else 'Default'}\n"
            f"Output Device: {output_device.name if output_device else 'Default'}\n"
            f"Sample Rate  : {config.sample_rate}\n"
            f"Channels     : {config.channels}\n"
            f"Block Size   : {config.block_size}"
        )
    
    if command.startswith("/audio input "):

        try:
            index = int(command.split()[-1])
        except ValueError:
            return "Usage: /audio input <index>"

        device = audio.set_input(index)

        if device is None:
            return "Input device not found."

        return f"Input device set to '{device.name}'."
    
    if command.startswith("/audio output "):

        try:
            index = int(command.split()[-1])
        except ValueError:
            return "Usage: /audio output <index>"

        device = audio.set_output(index)

        if device is None:
            return "Output device not found."

        return f"Output device set to '{device.name}'."
    

    if command == "/audio list":

        output = []

        output.append("=== Input Devices ===")

        for device in audio.input_devices():
            output.append(f"{device.id}: {device.name}")

        output.append("")
        output.append("=== Output Devices ===")

        for device in audio.output_devices():
            output.append(f"{device.id}: {device.name}")

        return "\n".join(output)
    
    if command.startswith("/audio input"):

        parts = command.split()

        if len(parts) != 3:
            return "Usage: /audio input <index>"

        try:
            index = int(parts[2])
        except ValueError:
            return "Device index must be a number."

        device = audio.set_input(index)

        if device is None:
            return "Input device not found."

        return f"Input device changed to '{device.name}'."
    
    if command.startswith("/audio output"):

        parts = command.split()

        if len(parts) != 3:
            return "Usage: /audio output <index>"

        try:
            index = int(parts[2])
        except ValueError:
            return "Device index must be a number."

        device = audio.set_output(index)

        if device is None:
            return "Output device not found."

        return f"Output device changed to '{device.name}'."

    return None