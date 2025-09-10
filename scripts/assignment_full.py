import sqlite3
from pathlib import Path
import random
import os

# -------------------------
# Setup database paths
# -------------------------
ROOT = Path(__file__).resolve().parent.parent
DB_DIR = ROOT / "db"
DB_DIR.mkdir(exist_ok=True)

USERS_DB = DB_DIR / "users.db"
PRODUCTS_DB = DB_DIR / "products.db"
ORDERS_DB = DB_DIR / "orders.db"

# -------------------------
# Function to create tables
# -------------------------
def create_tables():
    # Users table
    conn = sqlite3.connect(USERS_DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT
        );
    """)
    conn.commit()
    conn.close()

    # Products table
    conn = sqlite3.connect(PRODUCTS_DB)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price REAL
        );
    """)
    conn.commit()
    conn.close()

    # Orders table
    conn = sqlite3.connect(ORDERS_DB)
    cur = conn.cursor()
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

# -------------------------
# Function to insert sample data if tables empty
# -------------------------
def insert_sample_data():
    # Users
    conn = sqlite3.connect(USERS_DB)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    if cur.fetchone()[0] == 0:
        users = [("Alice", "alice@example.com"),
                 ("Bob", "bob@example.com"),
                 ("Charlie", "charlie@example.com")]
        cur.executemany("INSERT INTO users (name, email) VALUES (?, ?)", users)
        conn.commit()
    conn.close()

    # Products
    conn = sqlite3.connect(PRODUCTS_DB)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM products")
    if cur.fetchone()[0] == 0:
        products = [("Laptop", 500), ("Phone", 300), ("Tablet", 200)]
        cur.executemany("INSERT INTO products (name, price) VALUES (?, ?)", products)
        conn.commit()
    conn.close()

    # Orders
    conn = sqlite3.connect(ORDERS_DB)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM orders")
    if cur.fetchone()[0] == 0:
        orders = [(1, 1, 2), (1, 2, 1), (2, 3, 5)]
        cur.executemany("INSERT INTO orders (user_id, product_id, quantity) VALUES (?, ?, ?)", orders)
        conn.commit()
    conn.close()

# -------------------------
# Function to view table data
# -------------------------
def view_tables():
    for db_file, table_name in [(USERS_DB, "users"), (PRODUCTS_DB, "products"), (ORDERS_DB, "orders")]:
        conn = sqlite3.connect(db_file)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {table_name}")
        rows = cur.fetchall()
        print(f"\n{table_name.capitalize()} Table:")
        for row in rows:
            print(row)
        conn.close()

# -------------------------
# Step 5: Queries
# -------------------------
def run_queries():
    # Step 5a: Retrieve orders for user_id = 1
    conn = sqlite3.connect(ORDERS_DB)
    cur = conn.cursor()
    user_id = 1
    cur.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
    orders = cur.fetchall()
    print(f"\nOrders for User ID {user_id}:")
    for order in orders:
        print(order)
    conn.close()

    # Step 5b: Detailed orders (manual join across databases)
    # Get users
    conn = sqlite3.connect(USERS_DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    users = {row[0]: (row[1], row[2]) for row in cur.fetchall()}  # id -> (name, email)
    conn.close()

    # Get products
    conn = sqlite3.connect(PRODUCTS_DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    products = {row[0]: (row[1], row[2]) for row in cur.fetchall()}  # id -> (name, price)
    conn.close()

    # Get orders
    conn = sqlite3.connect(ORDERS_DB)
    cur = conn.cursor()
    cur.execute("SELECT * FROM orders")
    orders = cur.fetchall()
    conn.close()

    # Print detailed orders
    print("\nDetailed Orders:")
    for order in orders:
        order_id, user_id, product_id, quantity = order
        user_name, user_email = users.get(user_id, ("Unknown", "Unknown"))
        product_name, product_price = products.get(product_id, ("Unknown", 0))
        print(order_id, user_name, user_email, product_name, product_price, quantity)

    # Step 5c: Update product price
    conn = sqlite3.connect(PRODUCTS_DB)
    cur = conn.cursor()
    product_id = 1
    new_price = 799.99
    cur.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, product_id))
    conn.commit()
    conn.close()
    print(f"\nUpdated product {product_id} price to {new_price}")

    # Step 5d: Delete user with id = 2
    conn = sqlite3.connect(USERS_DB)
    cur = conn.cursor()
    user_id = 2
    cur.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    print(f"\nDeleted user with ID {user_id}")

    # Step 5e: Count total orders
    conn = sqlite3.connect(ORDERS_DB)
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM orders")
    count = cur.fetchone()[0]
    conn.close()
    print(f"\nTotal orders: {count}")

# -------------------------
# Main Execution
# -------------------------
if __name__ == "__main__":
    create_tables()
    insert_sample_data()
    view_tables()
    run_queries()
