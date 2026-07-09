from core.database import Database


class Memory:

    def __init__(self):
        self.db = Database()

    def remember(self, key: str, value: str):
        self.db.cursor.execute(
            """
            INSERT OR REPLACE INTO memories (key, value)
            VALUES (?, ?)
            """,
            (key, value)
        )

        self.db.connection.commit()

    def recall(self, key: str):
        self.db.cursor.execute(
            """
            SELECT value
            FROM memories
            WHERE key = ?
            """,
            (key,)
        )

        result = self.db.cursor.fetchone()

        if result:
            return result[0]

        return None

    def forget(self, key: str):
        self.db.cursor.execute(
            """
            DELETE FROM memories
            WHERE key = ?
            """,
            (key,)
        )

    def list_memories(self):
        self.db.cursor.execute("""
            SELECT key, value
            FROM memories
            ORDER BY key
        """)

        return self.db.cursor.fetchall()
        
        
        self.db.connection.commit()