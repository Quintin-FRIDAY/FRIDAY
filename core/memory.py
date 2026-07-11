from core.database import Database


class Memory:
    """Stores and retrieves persistent key-value memories."""

    def __init__(self):
        self.db = Database()

    def remember(self, key: str, value: str):
        self.db.execute(
            """
            INSERT OR REPLACE INTO memories (key, value)
            VALUES (?, ?)
            """,
            (key, value)
        )

    def recall(self, key: str):
        result = self.db.fetchone(
            """
            SELECT value
            FROM memories
            WHERE key = ?
            """,
            (key,)
        )

        if result:
            return result[0]

        return None

    def forget(self, key: str):
        self.db.execute(
            """
            DELETE FROM memories
            WHERE key = ?
            """,
            (key,)
        )

    def list_memories(self):
        return self.db.fetchall(
            """
            SELECT key, value
            FROM memories
            """
        )


if __name__ == "__main__":
    memory = Memory()

    print("Saving memory...")
    memory.remember("name", "Quintin")

    print("Recalling memory...")
    print(memory.recall("name"))

    print("\nListing memories...")
    for key, value in memory.list_memories():
        print(f"{key} = {value}")

    print("\nDeleting memory...")
    memory.forget("name")

    print("\nChecking again...")
    print(memory.recall("name"))

    memory.db.close()