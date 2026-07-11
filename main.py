import traceback

from config import settings
from core.events import event_bus
import core.event_logger

from core.assistant import Friday
from core.brain import Brain
from core.history import History
from core.logger import log
from core.managers import settings_manager
from core.managers.settings_manager import SettingsManager

from core.container_instance import container


def main():
    # Create core components
    friday = Friday()
    brain = Brain()
    history = History()
    settings = SettingsManager()

    settings_manager.load()

    # Register components in the Dependency Injection Container
    container.register("assistant", friday)
    container.register("brain", brain)
    container.register("history", history)
    container.register("event_bus", event_bus)
    container.register("settings", settings)

    log("Application started.")

    friday.boot()
    friday.introduce()

    while True:
        command = input("You > ")

        event_bus.emit(
            "user_command",
            command=command
        )

        log(f"User: {command}")
        history.add("User", command)

        if command.lower() in ["exit", "quit", "shutdown"]:
            friday.shutdown()
            log("Application stopped.")
            break

        try:
            response = brain.process(command)

            event_bus.emit(
                "assistant_response",
                response=response
            )

            log(f"F.R.I.D.A.Y.: {response}")
            history.add("Assistant", response)

            print(f"\nF.R.I.D.A.Y. > {response}\n")

        except Exception as error:
            log(f"Error while processing '{command}': {error}", "ERROR")
            log(traceback.format_exc(), "ERROR")

            print("\nF.R.I.D.A.Y. > Sorry, something went wrong.\n")


if __name__ == "__main__":
    main()