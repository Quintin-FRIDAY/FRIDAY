from core.memory import Memory
from core.normalizer import normalize_occupation

memory = Memory()


def extract_occupation(text: str):
    """Extracts the user's occupation."""

    text = text.strip()
    lower = text.lower()

    patterns = [
        "i am a ",
        "i'm a ",
        "i am an ",
        "i'm an ",
        "i work as a ",
        "i work as an ",
    ]

    for prefix in patterns:

        if lower.startswith(prefix):

            occupation = normalize_occupation(
                text[len(prefix):]
            )

            memory.remember("occupation", occupation)

            return f"I'll remember that you're a {occupation}."

    return None