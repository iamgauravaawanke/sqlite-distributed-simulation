# 🗂️ SQLite Distributed Simulation

This project simulates a distributed system where different types of data are stored in separate SQLite databases.  
It demonstrates **multi-threaded insertions** into multiple databases at the same time.

---

## 📂 Databases
- **users.db** → Stores user details (`id`, `name`, `email`)  
- **products.db** → Stores product details (`id`, `name`, `price`)  
- **orders.db** → Stores order details (`id`, `user_id`, `product_id`)  

---

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/iamgauravaawanke/sqlite-distributed-simulation.git
   cd sqlite-distributed-simulation
