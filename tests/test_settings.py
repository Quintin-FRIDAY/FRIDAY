from core.managers.settings_manager import SettingsManager

settings = SettingsManager()

settings.load()

print(settings.get("assistant_name"))

settings.set("theme", "light")

settings.save()

print(settings.get("theme"))