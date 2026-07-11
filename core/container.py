"""
Project F.R.I.D.A.Y.
Dependency Injection Container
"""

from typing import Any


class Container:
    """
    Simple dependency injection container.
    """

    def __init__(self):
        self._services: dict[type, Any] = {}

    def register(self, service_type: type, instance: Any):
        """
        Register a service instance.
        """

        self._services[service_type] = instance

    def resolve(self, service_type: type) -> Any:
        """
        Resolve a registered service.
        """

        if service_type not in self._services:
            raise KeyError(
                f"Service '{service_type.__name__}' is not registered."
            )

        return self._services[service_type]

    def exists(self, service_type: type) -> bool:
        """
        Check whether a service is registered.
        """

        return service_type in self._services

    def unregister(self, service_type: type):
        """
        Remove a service.
        """

        self._services.pop(service_type, None)

    def clear(self):
        """
        Remove every registered service.
        """

        self._services.clear()

    def registered_services(self) -> list[str]:
        """
        Return the names of all registered services.
        """

        return [
            service.__name__
            for service in self._services.keys()
        ]