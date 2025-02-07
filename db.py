import sqlite3
from datetime import timedelta, datetime

import os

db_file = 'database/database.db'
os.makedirs(os.path.dirname(db_file), exist_ok=True)

def get_db():
    return sqlite3.connect(db_file)

def init_db():
    with get_db() as conn:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS polls
                    (id TEXT PRIMARY KEY, 
                    question TEXT not null,
                    creation_date TEXT not null,
                    expiration_date TEXT not null
                  )''')
        c.execute('''CREATE TABLE IF NOT EXISTS options
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    poll_id INTEGER,
                    option TEXT not null,
                    votes INTEGER default 0,
                    FOREIGN KEY(poll_id) REFERENCES polls(id)
                  )''')
        conn.commit()

def create_poll(id,question, expiration_date):
    current_date = datetime.now().strftime('%Y-%m-%d')
    with get_db() as conn:
        c = conn.cursor()
        c.execute('INSERT INTO polls (id, question, creation_date, expiration_date) VALUES (?, ?, ?, ?)', (id, question, current_date, expiration_date))
        conn.commit()


def get_polls():
    with get_db() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM polls')
        return c.fetchall()

def get_options(poll_id):
    with get_db() as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM options WHERE poll_id = ?', (poll_id,))
        return c.fetchall()

def add_option(poll_id, option):
    with get_db() as conn:
        c = conn.cursor()
        c.execute('INSERT INTO options (poll_id, option) VALUES (?, ?)', (poll_id, option))
        conn.commit()

def vote(poll_id, option_id):
    with get_db() as conn:
        c = conn.cursor()
        c.execute('UPDATE options SET votes = votes + 1 WHERE poll_id = ? AND id = ?', (poll_id, option_id))
        conn.commit()