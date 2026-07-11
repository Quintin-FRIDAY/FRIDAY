from core.database import Database


class History:
    """Stores and retrieves conversation history."""

    def __init__(self):
        self.db = Database()

    def add(self, role: str, message: str):
        self.db.execute(
            """
            INSERT INTO conversations (role, message)
            VALUES (?, ?)
            """,
            (role, message)
        )

    def latest(self, limit: int = 10):
        rows = self.db.fetchall(
            """
            SELECT role, message
            FROM conversations
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        return list(reversed(rows))

    def count(self):
        result = self.db.fetchone(
            """
            SELECT COUNT(*)
            FROM conversations
            """
        )

        return result[0]

    def clear(self):
        self.db.execute(
            """
            DELETE FROM conversations
            """
        )