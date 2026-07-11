from config.settings import APP_NAME, VERSION
from core.logger import log

print(APP_NAME)
print(VERSION)


class Friday:
    """Represents the F.R.I.D.A.Y. assistant and manages startup, shutdown, and user interaction."""
    
    def __init__(self):
        self.name = APP_NAME
        self.version = VERSION

    def boot(self):
        log("=" * 50)
        log(f"Starting {self.name}")
        log(f"Version {self.version}")
        log("Systems online.")
        log("Awaiting commands.")

    def shutdown(self):
        log("Shutting down...")

    def introduce(self):
        print()
        print("Hello.")
        print("I am F.R.I.D.A.Y.")
        print("Your personal artificial intelligence assistant.")
        print("All systems are functioning normally.")
        print()