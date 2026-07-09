from core.database import Database


class History:

    def __init__(self):
        self.db = Database()

    def add(self, role: str, message: str):
        self.db.cursor.execute(
            """
            INSERT INTO conversations (role, message)
            VALUES (?, ?)
            """,
            (role, message)
        )

        self.db.connection.commit()

    def latest(self, limit: int = 10):
        self.db.cursor.execute(
            """
            SELECT role, message
            FROM conversations
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,)
        )

        rows = self.db.cursor.fetchall()

        return list(reversed(rows))

    def count(self):
        self.db.cursor.execute(
            """
            SELECT COUNT(*)
            FROM conversations
            """
        )

        return self.db.cursor.fetchone()[0]

    def clear(self):
        self.db.cursor.execute(
            """
            DELETE FROM conversations
            """
        )

        self.db.connection.commit()