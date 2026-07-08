def run(command: str):
    greetings = {
        "hello",
        "hi",
        "hey",
        "good morning",
        "good afternoon",
        "good evening",
    }

    if command.lower() in greetings:
        return "Hello, Quintin."

    return None