"""
Plugin Metadata Model
Project F.R.I.D.A.Y.
"""

from dataclasses import dataclass


@dataclass(slots=True)
class PluginMetadata:
    """
    Represents metadata loaded from plugin.json.
    """

    name: str
    id: str
    version: str
    author: str
    description: str
    enabled: bool
    minimum_friday_version: str