import traceback

from core.assistant import Friday
from core.brain import Brain
from core.history import History
from core.logger import log


def main():
    friday = Friday()
    brain = Brain()
    history = History()

    log("Application started.")

    friday.boot()
    friday.introduce()

    while True:
        command = input("You > ")

        log(f"User: {command}")
        history.add("User", command)

        if command.lower() in ["exit", "quit", "shutdown"]:
            friday.shutdown()
            log("Application stopped.")
            break

        try:
            response = brain.process(command)

            log(f"F.R.I.D.A.Y.: {response}")
            history.add("Assistant", response)

            print(f"\nF.R.I.D.A.Y. > {response}\n")

        except Exception as error:
            log(f"Error while processing '{command}': {error}", "ERROR")
            log(traceback.format_exc(), "ERROR")

            print("\nF.R.I.D.A.Y. > Sorry, something went wrong.\n")


if __name__ == "__main__":
    main()