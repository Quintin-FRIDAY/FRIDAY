from core.logger import log
from config.settings import APP_NAME, VERSION

class Friday:

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