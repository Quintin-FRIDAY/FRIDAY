from core.commands import process
from ai.engine import AIEngine
from core.devtools.router import process as dev_process
from core.memory_extractor import MemoryExtractor
from core.recall import recall_memory

class Brain:
    """Coordinates memory extraction, developer tools, commands, and AI responses."""

    def __init__(self):
        self.ai = AIEngine()
        self.extractor = MemoryExtractor()

    def process(self, command: str) -> str:

        # 1. Try to learn something from the user's message
        memory_response = self.extractor.process(command)

        if memory_response is not None:
            return memory_response

        # 2. Recall information from memory
        recall_response = recall_memory(command)

        if recall_response is not None:
            return recall_response

        # 3. Developer commands
        response = dev_process(command)

        if response is not None:
            return response

        # 3. Built-in commands
        response = process(command)

        if response is not None:
            return response

        # 4. Fall back to the AI
        return self.ai.ask(command)