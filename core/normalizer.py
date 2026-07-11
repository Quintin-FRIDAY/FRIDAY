def normalize_text(text: str) -> str:
    """
    Cleans text before it is stored as long-term memory.
    """

    text = text.strip()

    # Remove trailing punctuation
    text = text.rstrip(".")

    # Remove duplicate spaces
    text = " ".join(text.split())

    return text


def normalize_name(name: str) -> str:
    """
    Formats names consistently.
    """

    name = normalize_text(name)

    return name.title()


def normalize_location(location: str) -> str:
    """
    Formats locations consistently.
    """

    location = normalize_text(location)

    return location.title()


def normalize_preference(value: str) -> str:
    """
    Formats preference values.
    """

    value = normalize_text(value)

    return value.title()


def normalize_occupation(job: str) -> str:
    """
    Formats occupations consistently.
    """

    job = normalize_text(job)

    return job.title()