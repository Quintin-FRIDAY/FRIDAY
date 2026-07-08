from core.assistant import Friday
from core.commands import process
from core.brain import Brain


def main():
    friday = Friday()
    brain = Brain()

    friday.boot()
    friday.introduce()

    while True:
        command = input("You > ")

        if command.lower() in ["exit", "quit", "shutdown"]:
            friday.shutdown()
            break

        response = process(command)

        if response == "I'm sorry, I don't know how to do that yet.":
            response = brain.think(command)

        print(f"\nF.R.I.D.A.Y. > {response}\n")


if __name__ == "__main__":
    main()