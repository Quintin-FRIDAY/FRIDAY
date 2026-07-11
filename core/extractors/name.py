from core.memory import Memory
from core.normalizer import normalize_name

memory = Memory()


def extract_name(text: str):
    """Extracts and stores the user's name."""

    text = text.strip()

    lower = text.lower()

    if lower.startswith("my name is "):

        name = normalize_name(text[11:])

        memory.remember("user_name", name)

        return f"Nice to meet you, {name}. I'll remember that."

    return None