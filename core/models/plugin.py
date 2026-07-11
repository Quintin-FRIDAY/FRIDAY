"""
Plugin Model
Project F.R.I.D.A.Y.
"""

from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

from core.models.plugin_metadata import PluginMetadata


@dataclass(slots=True)
class Plugin:
    """
    Represents a loaded plugin.
    """

    metadata: PluginMetadata
    module: ModuleType | None
    path: Path

    loaded: bool = False
    error: str | None = None