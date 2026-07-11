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

    def register(self, name: str, instance):
        """
        Register a service instance.
        """

        self._services[name] = instance

    def resolve(self, name: str):
        """
        Resolve a registered service.
        """

        if name not in self._services:
            raise KeyError(f"Service '{name}' is not registered.")

        return self._services[name]

    def exists(self, name: str) -> bool:
        """
        Check whether a service exists.
        """

        return name in self._services