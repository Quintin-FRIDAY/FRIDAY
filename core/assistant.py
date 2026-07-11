from config.settings import APP_NAME, VERSION
from core.logger import log
from core.events import event_bus

print(APP_NAME)
print(VERSION)


class Friday:
    """Represents the F.R.I.D.A.Y. assistant and manages startup, shutdown, and user interaction."""

    def __init__(self):
        self.name = APP_NAME
        self.version = VERSION

    def boot(self):
        event_bus.emit(
            "assistant_started",
            version=self.version
        )

        log("=" * 50)
        log(f"Starting {self.name}")
        log(f"Version {self.version}")
        log("Systems online.")
        log("Awaiting commands.")

    def shutdown(self):
        event_bus.emit("assistant_stopped")

        log("Shutting down...")

    def introduce(self):
        print()
        print("Hello.")
        print("I am F.R.I.D.A.Y.")
        print("Your personal artificial intelligence assistant.")
        print("All systems are functioning normally.")
        print()

        event_bus.emit(
            "assistant_introduced",
            assistant=self.name
        )