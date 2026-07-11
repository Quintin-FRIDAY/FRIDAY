"""
Project F.R.I.D.A.Y.
Service Manager
"""

from core.models.service import Service


class ServiceManager:
    """
    Starts, stops and manages every service.
    """

    def __init__(self):
        self.services: list[Service] = []

    def register(self, name: str, instance: object):
        """
        Register a service.
        """

        self.services.append(
            Service(
                name=name,
                instance=instance
            )
        )
    
    def start(self):
        """
        Start every registered service.
        """

        for service in self.services:

            if hasattr(service.instance, "start"):

                try:

                    service.instance.start()
                    service.started = True

                except Exception as error:

                    service.error = str(error)

    def stop(self):
        """
        Stop every service.
        """

        for service in reversed(self.services):

            if hasattr(service.instance, "stop"):

                try:

                    service.instance.stop()
                    service.started = False

                except Exception as error:

                    service.error = str(error)

    def status(self):

        for service in self.services:

            print(
                f"{service.name}: "
                f"{'Running' if service.started else 'Stopped'}"
            )

    def reload(self):

        self.stop()
        self.start()