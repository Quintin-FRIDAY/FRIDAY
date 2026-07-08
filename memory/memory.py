import json
from pathlib import Path


class Memory:

    def __init__(self):
        self.file = Path("data/memory.json")

        if not self.file.exists():
            self.file.parent.mkdir(exist_ok=True)
            self.file.write_text("{}")

    def load(self):
        return json.loads(self.file.read_text())

    def save(self, key, value):
        data = self.load()
        data[key] = value
        self.file.write_text(json.dumps(data, indent=4))