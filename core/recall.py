from core.memory import Memory

memory = Memory()


def recall_memory(command: str):
    """
    Answers questions using long-term memory.
    """

    text = command.lower().strip()

    questions = {
        "what's my name": (
            "user_name",
            "Your name is {}."
        ),

        "what is my name": (
            "user_name",
            "Your name is {}."
        ),

        "where do i live": (
            "user_location",
            "You live in {}."
        ),

        "where am i from": (
            "user_hometown",
            "You're from {}."
        ),

        "what is my occupation": (
            "occupation",
            "You're a {}."
        ),

        "what's my occupation": (
            "occupation",
            "You're a {}."
        ),

        "what is my favorite game": (
            "favorite_game",
            "Your favorite game is {}."
        ),

        "what's my favorite game": (
            "favorite_game",
            "Your favorite game is {}."
        ),

        "what is my favourite game": (
            "favorite_game",
            "Your favorite game is {}."
        ),

        "what's my favourite game": (
            "favorite_game",
            "Your favorite game is {}."
        ),
    }

    for question, (key, response) in questions.items():

        if text == question:

            value = memory.recall(key)

            if value:
                return response.format(value)

            return "I don't know yet."

    return None