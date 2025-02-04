import sqlite3

db_file = 'database.db'

def get_db():
    return sqlite3.connect(db_file)

def init_db():
    with sqlite3.connect(db_file) as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS polls (
            id TEXT PRIMARY KEY,
            question TEXT NOT NULL
        )
        """)
        c.execute("""
        CREATE TABLE IF NOT EXISTS options (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            poll_id TEXT NOT NULL,
            option_text TEXT NOT NULL,
            votes INTEGER DEFAULT 0,
            FOREIGN KEY (poll_id) REFERENCES polls(id)
        )
        """)
