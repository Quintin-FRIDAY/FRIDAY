from core.commands import process
from core.devtools.router import process as dev_process
from ai.engine import AIEngine


class Brain:
    """Coordinates developer tools, built-in commands, and AI-generated responses."""

    def __init__(self):
        self.ai = AIEngine()

    def process(self, command: str) -> str:
        # Check developer commands first
        response = dev_process(command)

        if response is not None:
            return response

        # Check built-in commands/skills
        response = process(command)

        if response is not None:
            return response

        # Fall back to the AI model
        return self.ai.ask(command)