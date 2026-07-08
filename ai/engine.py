from ollama import chat


class AIEngine:
    def __init__(self, model="gemma3:4b"):
        self.model = model

    def ask(self, prompt: str) -> str:
        try:
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

        except Exception as e:
            return f"AI Error: {e}"