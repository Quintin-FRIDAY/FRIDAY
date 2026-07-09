from core.history import History

history = History()


def process_history(command: str):

    if not command.startswith("/history"):
        return None

    if command == "/history count":
        return f"Conversation count: {history.count()}"

    if command == "/history clear":
        history.clear()
        return "Conversation history cleared."

    if command == "/history latest":
        conversations = history.latest()

        if not conversations:
            return "No conversation history."

        output = []

        for row in conversations:
            output.append(f"{row['role']}: {row['message']}")

        return "\n".join(output)

    return None