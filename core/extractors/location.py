from core.memory import Memory
from core.normalizer import normalize_location

memory = Memory()


def extract_location(text: str):
    """Extracts the user's location from natural language."""

    text = text.strip()
    lower = text.lower()

    # Pattern: I live in ...
    if lower.startswith("i live in "):
        location = normalize_location(text[10:])

        memory.remember("user_location", location)

        return f"I'll remember that you live in {location}."

    # Pattern: I am from ...
    if lower.startswith("i am from "):
        location = normalize_location(text[10:])

        memory.remember("user_hometown", location)

        return f"I'll remember that you're from {location}."

    return None