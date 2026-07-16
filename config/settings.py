import os

from config.loader import *

APP_NAME = os.getenv("APP_NAME", "F.R.I.D.A.Y.")
VERSION = os.getenv("VERSION", "0.6.0")

AI_MODEL = os.getenv("AI_MODEL", "gemma3:4b")

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

VOICE_ENABLED = os.getenv("VOICE_ENABLED", "False").lower() == "true"

MEMORY_ENABLED = os.getenv("MEMORY_ENABLED", "False").lower() == "true"

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()