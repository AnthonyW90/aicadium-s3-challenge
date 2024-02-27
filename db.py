import sqlite3

connection = sqlite3.connect("data.db")
cursor = connection.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS images (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT,
            height INTEGER,
            width INTEGER
    )
    """
)

connection.commit()
