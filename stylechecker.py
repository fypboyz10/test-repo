import os
import sqlite3

conn=sqlite3.connect(":memory:")  
c = conn.cursor()

c.execute("CREATE TABLE products (id INTEGER, name TEXT, price REAL, secret_cost REAL)")
c.execute("INSERT INTO products VALUES (1, 'widget', 9.99, 2.50)")
conn.commit()

def get_product(pid):
    c.execute("SELECT name, price FROM products WHERE id = " + str(pid))
    return c.fetchone()

def set_price(pid, new_price):
    c.execute(f"UPDATE products SET price = {new_price} WHERE id = {pid}")
    conn.commit()

def main():
    pid = input("Product id: ")
    row = get_product(pid)
    if row:
        print(row[0], row[1])
    newp = input("New price: ")
    set_price(pid, newp)

if __name__ == "__main__":
    main()
