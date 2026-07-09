from core.devtools.memory import process_memory
from core.devtools.history import process_history


def process(command: str):

    response = process_memory(command)

    if response is not None:
        return response

    response = process_history(command)

    if response is not None:
        return response

    return None