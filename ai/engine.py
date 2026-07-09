from ollama import chat
from config.settings import AI_MODEL


class AIEngine:

    def __init__(self, model=AI_MODEL):
        self.model = model

    def ask(self, prompt: str) -> str:
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]