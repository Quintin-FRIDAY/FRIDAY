from core.memory import Memory
from core.normalizer import normalize_preference

memory = Memory()


def extract_preferences(text: str):
    """Extracts user preferences from natural language."""

    text = text.strip()

    lower = text.lower()

    patterns = [
        ("my favourite ", "my favourite "),
        ("my favorite ", "my favorite ")
    ]

    for _, prefix in patterns:

        if lower.startswith(prefix):

            sentence = text[len(prefix):]

            if " is " not in sentence:
                continue

            category, value = sentence.split(" is ", 1)

            category = category.strip().replace(" ", "_")
            value = normalize_preference(value)

            key = f"favorite_{category}"

            memory.remember(key, value)

            return f"I'll remember that your favourite {category.replace('_', ' ')} is {value}."

    return None