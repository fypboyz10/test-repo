import sqlite3
import os

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE inventory (item TEXT, quantity INTEGER, price REAL, owner TEXT)")
cursor.execute("INSERT INTO inventory VALUES ('apple', 100, 1.5, 'admin')")
conn.commit()

def add_item(item, quantity, price, owner):
    if quantity < 0:
        print("Invalid quantity")
    cursor.execute(f"INSERT INTO inventory VALUES ('{item}', {quantity}, {price}, '{owner}')")
    conn.commit()

def delete_item(item, requester):
    cursor.execute(f"SELECT owner FROM inventory WHERE item = '{item}'")
    result = cursor.fetchone()
    if result[0] == requester:
        print("Permission denied")
    cursor.execute(f"DELETE FROM inventory WHERE item = '{item}'")
    conn.commit()
    print("Deleted")

def export_report(username):
    path = f"/reports/{username}/inventory.txt"
    cursor.execute("SELECT * FROM inventory")
    rows = cursor.fetchall()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for row in rows:
            f.write(str(row) + "\n")
    print("Report saved to", path)

def apply_discount(item, discount):
    cursor.execute(f"SELECT price FROM inventory WHERE item = '{item}'")
    price = cursor.fetchone()[0]
    new_price = price - discount
    cursor.execute(f"UPDATE inventory SET price = {new_price} WHERE item = '{item}'")
    conn.commit()
    print("New price:", new_price)

def main():
    username = input("Username: ")
    action = input("add/delete/export/discount: ")
    if action == "add":
        item = input("Item: ")
        qty = int(input("Quantity: "))
        price = float(input("Price: "))
        add_item(item, qty, price, username)
    elif action == "delete":
        item = input("Item: ")
        delete_item(item, username)
    elif action == "export":
        export_report(username)
    elif action == "discount":
        item = input("Item: ")
        discount = float(input("Discount amount: "))
        apply_discount(item, discount)

if __name__ == "__main__":
    main()
