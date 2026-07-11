"""
Project F.R.I.D.A.Y.
Settings Manager
"""

import json
from pathlib import Path


class SettingsManager:
    """
    Loads and saves application settings.
    """

    def __init__(self):
        self.file = Path("config/settings.json")
        self.settings = {}

    def load(self):
        """
        Load settings from disk.
        """

        if not self.file.exists():
            self.create_default_settings()

        with open(self.file, "r", encoding="utf-8") as file:
            self.settings = json.load(file)

    def save(self):
        """
        Save settings to disk.
        """

        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(
                self.settings,
                file,
                indent=4
            )

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value

    def create_default_settings(self):
        """
        Create default settings.
        """

        defaults = {
            "assistant_name": "F.R.I.D.A.Y.",
            "theme": "dark",
            "voice_enabled": False,
            "memory_enabled": True,
            "debug": True
        }

        self.file.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file, "w", encoding="utf-8") as file:
            json.dump(
                defaults,
                file,
                indent=4
            )