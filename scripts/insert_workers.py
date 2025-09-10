import sqlite3
import threading
import random
from pathlib import Path



#Root project folder
ROOT = Path(__file__).resolve().parent.parent  

# Database folder
DB_DIR = ROOT / "db"

# Paths to each database
USERS_DB = DB_DIR / "users.db"
PRODUCTS_DB = DB_DIR / "products.db"
ORDERS_DB = DB_DIR / "orders.db"


# Insert a user into users.db
def insert_user(name, email):
    conn = sqlite3.connect(USERS_DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()

# Insert a product into products.db
def insert_product(name, price):
    conn = sqlite3.connect(PRODUCTS_DB)
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price) VALUES (?, ?)", (name, price))
    conn.commit()
    conn.close()

# Insert an order into orders.db
def insert_order(user_id, product_id, quantity):
    conn = sqlite3.connect(ORDERS_DB)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO orders (user_id, product_id, quantity) VALUES (?, ?, ?)",
        (user_id, product_id, quantity)
    )
    conn.commit()
    conn.close()

# Sample user names and emails
user_names = ["Alice", "Bob", "Charlie", "David", "Eva"]

# Sample product names
product_names = ["Laptop", "Phone", "Tablet", "Headphones", "Camera"]

# Number of entries to insert
NUM_INSERTS = 10

threads = []

# Insert users
for i in range(NUM_INSERTS):
    name = random.choice(user_names) + str(i)  # e.g., Alice0, Bob1
    email = f"user{i}@example.com"
    t = threading.Thread(target=insert_user, args=(name, email))
    threads.append(t)
    t.start()

# Insert products
for i in range(NUM_INSERTS):
    name = random.choice(product_names) + str(i)
    price = round(random.uniform(100, 1000), 2)  # Random price
    t = threading.Thread(target=insert_product, args=(name, price))
    threads.append(t)
    t.start()

# Insert orders (random user_id and product_id)
for i in range(NUM_INSERTS):
    user_id = random.randint(1, NUM_INSERTS)      # Assuming user IDs 1-10
    product_id = random.randint(1, NUM_INSERTS)   # Assuming product IDs 1-10
    quantity = random.randint(1, 5)
    t = threading.Thread(target=insert_order, args=(user_id, product_id, quantity))
    threads.append(t)
    t.start()
# Wait for all threads to complete
for t in threads:
    t.join()

print(f"Inserted {NUM_INSERTS} users, products, and orders successfully!")
