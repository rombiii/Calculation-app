import sqlite3
from config import Config

def init_db():
    conn = sqlite3.connect("balance.db") #TODO Change this hardcoded DB Name to this one from .env
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS transactions
                   (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       type TEXT NOT NULL,
                       amount REAL NOT NULL,
                       timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                   )
                   ''')
    conn.commit()
    conn.close()

def add_balance(amount, trans_type):
    conn = sqlite3.connect("balance.db")
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO transactions (type, amount)
                   VALUES (?, ?)
                   ''', (trans_type, amount))
    conn.commit()
    conn.close()

def get_balance():
    conn = sqlite3.connect("balance.db")
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT SUM(CASE WHEN type = 'income' THEN amount ELSE -amount END)
                   FROM transactions
                   ''')
    result = cursor.fetchone()[0]
    conn.close()
    return result or 0.0

def get_history():
    conn = sqlite3.connect("balance.db")
    cursor = conn.cursor()
    cursor.execute('''
        SELECT id, type, amount, timestamp FROM transactions ORDER BY timestamp DESC
    ''')
    rows = cursor.fetchall()
    conn.close()
    return rows
