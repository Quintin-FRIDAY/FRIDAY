from datetime import datetime

def run(command: str):
    command = command.lower()

    if "time" in command:
        return datetime.now().strftime("The current time is %H:%M:%S.")

    if "date" in command:
        return datetime.now().strftime("Today is %A, %d %B %Y.")

    return None