"""
Project F.R.I.D.A.Y.
Plugin Manager
"""

from pathlib import Path
import json
import importlib.util

from core.models.plugin import Plugin
from core.models.plugin_metadata import PluginMetadata
from core.events import event_bus


class PluginManager:
    """
    Responsible for discovering, loading, managing,
    and executing F.R.I.D.A.Y. plugins.
    """

    def __init__(self):
        self.plugin_directory = Path("plugins")
        self.plugins: list[Plugin] = []

    def discover_plugins(self) -> list[Path]:
        """
        Discover all plugin folders.
        """

        if not self.plugin_directory.exists():
            return []

        return [
            folder
            for folder in self.plugin_directory.iterdir()
            if folder.is_dir()
        ]

    def load_metadata(self, plugin_folder: Path) -> PluginMetadata | None:
        """
        Load plugin metadata from plugin.json.
        """

        metadata_file = plugin_folder / "plugin.json"

        if not metadata_file.exists():
            return None

        with open(metadata_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        return PluginMetadata(
            name=data["name"],
            id=data["id"],
            version=data["version"],
            author=data["author"],
            description=data["description"],
            enabled=data["enabled"],
            minimum_friday_version=data["minimum_friday_version"],
        )

    def load_plugin(self, plugin_folder: Path) -> Plugin | None:
        """
        Safely load a plugin.
        """

        metadata = self.load_metadata(plugin_folder)

        if metadata is None:
            return None

        if not metadata.enabled:
            return None

        plugin_file = plugin_folder / "plugin.py"

        if not plugin_file.exists():
            return None

        try:
            spec = importlib.util.spec_from_file_location(
                metadata.id,
                plugin_file
            )

            if spec is None or spec.loader is None:
                raise ImportError("Unable to create module specification.")

            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            required_functions = [
                "can_handle",
                "handle"
            ]

            for function_name in required_functions:
                if not hasattr(module, function_name):
                    raise AttributeError(
                        f"Plugin '{metadata.name}' is missing '{function_name}()'"
                    )

            # Optional startup hook
            if hasattr(module, "startup"):
                module.startup()

            event_bus.emit(
                "plugin_loaded",
                plugin=metadata.name,
                version=metadata.version
            )

            return Plugin(
                metadata=metadata,
                module=module,
                path=plugin_folder,
                loaded=True
            )

        except Exception as error:

            event_bus.emit(
                "plugin_failed",
                plugin=metadata.name,
                error=str(error)
            )

            return Plugin(
                metadata=metadata,
                module=None,
                path=plugin_folder,
                loaded=False,
                error=str(error)
            )

    def load_plugins(self):
        """
        Load all plugins.
        """

        self.plugins.clear()

        for folder in self.discover_plugins():

            plugin = self.load_plugin(folder)

            if plugin:
                self.plugins.append(plugin)

    def process(self, command: str) -> str | None:
        """
        Give each loaded plugin a chance to handle a command.
        """

        event_bus.emit(
            "command_received",
            command=command
        )

        for plugin in self.loaded_plugins:

            try:

                if plugin.module.can_handle(command):

                    event_bus.emit(
                        "command_handled",
                        plugin=plugin.metadata.name,
                        command=command
                    )

                    return plugin.module.handle(command)

            except Exception as error:

                plugin.loaded = False
                plugin.error = str(error)

        event_bus.emit(
            "command_unhandled",
            command=command
        )

        return None

    def shutdown_plugins(self):
        """
        Shutdown all loaded plugins.
        """

        for plugin in self.loaded_plugins:

            try:

                if hasattr(plugin.module, "shutdown"):
                    plugin.module.shutdown()

            except Exception as error:

                plugin.error = str(error)

    def reload_plugins(self):
        """
        Reload every plugin.
        """

        self.shutdown_plugins()
        self.load_plugins()

    def list_plugins(self) -> list[PluginMetadata]:
        """
        Return metadata for all loaded plugins.
        """

        return [
            plugin.metadata
            for plugin in self.loaded_plugins
        ]

    @property
    def loaded_plugins(self) -> list[Plugin]:
        """
        Return only successfully loaded plugins.
        """

        return [
            plugin
            for plugin in self.plugins
            if plugin.loaded
        ]