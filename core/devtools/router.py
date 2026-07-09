from core.devtools.memory import process_memory


def process(command: str):

    response = process_memory(command)

    if response is not None:
        return response

    return None
