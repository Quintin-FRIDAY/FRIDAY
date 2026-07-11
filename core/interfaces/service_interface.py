"""
Project F.R.I.D.A.Y.
Service Interface
"""

from abc import ABC, abstractmethod


class ServiceInterface(ABC):
    """
    Base interface for all F.R.I.D.A.Y. services.
    """

    @abstractmethod
    def start(self) -> None:
        """
        Start the service.
        """
        raise NotImplementedError

    @abstractmethod
    def stop(self) -> None:
        """
        Stop the service.
        """
        raise NotImplementedError

    def reload(self) -> None:
        """
        Reload the service.
        """

        self.stop()
        self.start()

    def health_check(self) -> bool:
        """
        Return whether the service is healthy.
        """

        return True