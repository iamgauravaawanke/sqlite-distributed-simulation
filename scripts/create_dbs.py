import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_DIR = ROOT / "db"
DB_DIR.mkdir(parents=True, exist_ok=True)

def create_users_db(path):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("PRAGMA journal_mode=WAL;")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        );
    """)
    conn.commit()
    conn.close()

def create_products_db(path):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("PRAGMA journal_mode=WAL;")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        );
    """)
    conn.commit()
    conn.close()

def create_orders_db(path):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute("PRAGMA journal_mode=WAL;")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            product_id INTEGER,
            quantity INTEGER
        );
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_users_db(DB_DIR / "users.db")
    create_products_db(DB_DIR / "products.db")
    create_orders_db(DB_DIR / "orders.db")
    print("Created users.db, products.db, orders.db in:", DB_DIR)
