from ai.engine import AIEngine


class Brain:
    def __init__(self):
        self.ai = AIEngine()

    def think(self, command: str) -> str:
        return self.ai.ask(command)