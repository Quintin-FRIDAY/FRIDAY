from config.settings import APP_NAME, VERSION

def run(command: str):
    command = command.lower()

    if command == "status":
        return "All systems operational."

    if command == "version":
        return f"{APP_NAME} v{VERSION}"

    if command == "help":
        return (
            "Available commands:\n"
            "- hello\n"
            "- time\n"
            "- date\n"
            "- status\n"
            "- version\n"
            "- help\n"
            "- shutdown"
        )

    return None