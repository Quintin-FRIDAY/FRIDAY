from core.commands import process
from ai.engine import AIEngine


class Brain:
    def __init__(self):
        self.ai = AIEngine()

    def process(self, command: str) -> str:
        response = process(command)

        if response is not None:
            return response

        return self.ai.ask(command)