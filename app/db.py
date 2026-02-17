import sqlite3
from config import DB_PATH

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()

cur.execute(
    """
CREATE TABLE IF NOT EXISTS products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
price REAL,
link TEXT
)
"""
)
conn.commit()


def save_products(items):
    for p in items:
        cur.execute(
            "INSERT INTO products(name,price,link) VALUES(?,?,?)",
            (p["name"], p["price"], p["link"]),
        )
    conn.commit()


def get_all():
    return cur.execute("SELECT * FROM products").fetchall()
