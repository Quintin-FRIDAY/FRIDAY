"""
Project F.R.I.D.A.Y.
Service Model
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Service:
    """
    Represents a managed service.
    """

    name: str
    instance: object

    started: bool = False
    enabled: bool = True
    error: str | None = None