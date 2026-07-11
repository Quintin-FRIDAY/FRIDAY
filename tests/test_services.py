import traceback

from core.managers.service_manager import ServiceManager


class TestService:

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")


manager = ServiceManager()

manager.register(
    "Test",
    TestService()
)

manager.start()
manager.status()
manager.stop()