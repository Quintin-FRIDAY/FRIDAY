"""
Example Plugin
Project F.R.I.D.A.Y.
"""


def startup():
    print("Example Plugin started.")


def shutdown():
    print("Example Plugin stopped.")


def can_handle(command: str) -> bool:
    return "example" in command.lower()


def handle(command: str) -> str:
    return "Example plugin executed successfully!"