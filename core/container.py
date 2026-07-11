"""
Project F.R.I.D.A.Y.
Dependency Injection Container
"""


class Container:
    """
    Simple dependency injection container.
    """

    def __init__(self):
        self._services = {}

    def register(self, key, instance):
        """
        Register a service instance.
        """

        self._services[key] = instance

    def resolve(self, key):
        """
        Resolve a registered service.
        """

        if key not in self._services:
            raise KeyError(
                f"Service '{key}' is not registered."
            )

        return self._services[key]

    def exists(self, key) -> bool:
        """
        Check whether a service exists.
        """

        return key in self._services

    def unregister(self, key):
        """
        Remove a service.
        """

        self._services.pop(key, None)

    def clear(self):
        """
        Remove every registered service.
        """

        self._services.clear()

    def registered_services(self):
        """
        Return every registered key.
        """

        return list(self._services.keys())