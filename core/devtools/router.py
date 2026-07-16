from core.devtools.memory import process_memory
from core.devtools.history import process_history
from core.devtools.audio import process_audio


def process(command: str):

    response = process_memory(command)

    if response is not None:
        return response

    response = process_history(command)

    if response is not None:
        return response

    response = process_audio(command)

    if response is not None:
        return response

    return None