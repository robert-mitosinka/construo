import psycopg2
import random

def create_test_data():
    conn = psycopg2.connect(
        host="mypgserver.postgres.database.azure.com",
        dbname="postgres",
        user="myadmin@mypgserver",
        password="MyPassword123",
        sslmode="require"
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name TEXT,
            price NUMERIC,
            stock INT
        )
    """)
    for _ in range(10):
        cur.execute(
            "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
            (f"Product {_}", round(random.uniform(10, 100), 2), random.randint(1, 50))
        )
    conn.commit()
    cur.close()
    conn.close()

