"""
Project F.R.I.D.A.Y.
Application Bootstrapper
"""

import traceback

import core.event_logger

from core.events import event_bus
from core.models.event_type import EventType
from core.logger import log

from core.assistant import Friday
from core.brain import Brain
from core.history import History

from core.managers.settings_manager import SettingsManager

from core.container_instance import container


class Bootstrapper:
    """
    Responsible for creating and initializing F.R.I.D.A.Y.
    """

    def __init__(self):

        self.friday = Friday()
        self.brain = Brain()
        self.history = History()

        log("Creating application bootstrapper...")

    def initialize(self):
        """
        Initialize the application.
        """

        log("Initializing application...")

        # Create core components
        self.friday = Friday()
        self.brain = Brain()
        self.history = History()
        self.settings_manager = SettingsManager()

        # Load settings
        self.settings_manager.load()

        # Register components
        container.register(Friday, self.friday)
        container.register(Brain, self.brain)
        container.register(History, self.history)
        container.register(SettingsManager, self.settings_manager)
        container.register(type(event_bus), event_bus)

    def run(self):
        """
        Start F.R.I.D.A.Y.
        """

        self.initialize()

        log("Application started.")

        self.friday.boot()
        self.friday.introduce()

        while True:
            command = input("You > ")

            event_bus.emit(
                EventType.USER_COMMAND,
                command=command
            )

            log(f"User: {command}")
            self.history.add("User", command)

            if command.lower() in ["exit", "quit", "shutdown"]:
                self.friday.shutdown()
                log("Application stopped.")
                break

            try:
                response = self.brain.process(command)

                event_bus.emit(
                    EventType.ASSISTANT_RESPONSE,
                    response=response
                )

                log(f"F.R.I.D.A.Y.: {response}")
                self.history.add("Assistant", response)

                print(f"\nF.R.I.D.A.Y. > {response}\n")

            except Exception as error:

                log(
                    f"Error while processing '{command}': {error}",
                    "ERROR"
                )

                log(
                    traceback.format_exc(),
                    "ERROR"
                )

                print(
                    "\nF.R.I.D.A.Y. > Sorry, something went wrong.\n"
                )