import sqlite3
from pathlib import Path

DB_DIR = Path(__file__).resolve().parent.parent / "db"
USERS_DB = DB_DIR / "users.db"

conn = sqlite3.connect(USERS_DB)
cur = conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cur.fetchall()
print("Tables in users.db:", tables)

conn.close()
