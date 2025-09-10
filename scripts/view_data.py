from pathlib import Path
import sqlite3

# Root project folder (one level above scripts/)
ROOT = Path(__file__).resolve().parent.parent
DB_DIR = ROOT / "db"

USERS_DB = DB_DIR / "users.db"

# Connect to the database
conn = sqlite3.connect(USERS_DB)
cur = conn.cursor()

# Query all rows in the users table
cur.execute("SELECT * FROM users")
rows = cur.fetchall()

print("Users Table:")
for row in rows:
    print(row)

conn.close()

PRODUCTS_DB = DB_DIR / "products.db"

conn = sqlite3.connect(PRODUCTS_DB)
cur = conn.cursor()

cur.execute("SELECT * FROM products")
rows = cur.fetchall()

print("\nProducts Table:")
for row in rows:
    print(row)

conn.close()


ORDERS_DB = DB_DIR / "orders.db"

conn = sqlite3.connect(ORDERS_DB)
cur = conn.cursor()

cur.execute("SELECT * FROM orders")
rows = cur.fetchall()

print("\nOrders Table:")
for row in rows:
    print(row)

conn.close()
