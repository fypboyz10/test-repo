import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE orders (order_id INTEGER, user TEXT, item TEXT, qty INTEGER, status TEXT)")
cursor.execute("INSERT INTO orders VALUES (1, 'alice', 'book', 2, 'pending')")
conn.commit()

def get_order(order_id):
    cursor.execute(f"SELECT * FROM orders WHERE order_id = {order_id}")
    return cursor.fetchone()

def cancel_order(order_id):
    cursor.execute(f"UPDATE orders SET status = 'cancelled' WHERE order_id = {order_id}")
    conn.commit()
    print("Order cancelled")

def apply_discount(price, discount_pct):
    discounted = price - (price * discount_pct / 100)
    return discounted

def main():
    user = input("Username: ")
    order_id = input("Order ID: ")
    order = get_order(order_id)

    if order == None:
        print("Order not found")
    elif order[1] != user:
        print("Not your order!")

    action = input("cancel/discount: ")
    if action == "cancel":
        cancel_order(order_id)
    elif action == "discount":
        price = float(input("Original price: "))
        pct = float(input("Discount %: "))
        print("Final price:", apply_discount(price, pct))

if __name__ == "__main__":
    main()
