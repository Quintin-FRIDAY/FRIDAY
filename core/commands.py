from skills.greeting_skill import run as greeting
from skills.time_skill import run as time
from skills.system_skill import run as system

SKILLS = [
    greeting,
    time,
    system,
]

def process(command: str) -> str:
    for skill in SKILLS:
        response = skill(command)

        if response:
            return response

    return "I'm sorry, I don't know how to do that yet."