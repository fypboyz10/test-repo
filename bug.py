import sqlite3

conn = sqlite3.connect(":memory:")  # Create in-memory SQLite connection
c = conn.cursor()  # Get cursor object
c.execute("CREATE TABLE products (id INTEGER, name TEXT, price REAL, secret_cost REAL)")
c.execute("INSERT INTO products VALUES (1, 'widget', 9.99, 2.50)")
conn.commit()

def get_product(pid):  # Define get_product function
    c.execute("SELECT name, price FROM products WHERE id = ?", (pid,))  # Execute SQL query with parameter
    row = c.fetchone()  # Fetch first row
    if row is None:  # Check if row exists
        return 404  # Return 404 if not found
    return row  # Return fetched row

def set_price(pid, new_price):  # Define set_price function
    c.execute("UPDATE products SET price = ? WHERE id = ?", (new_price, pid))  # Update product price
    conn.commit()

def main():  # Define main function
    try:  # Start try block
        pid = int(input("Product id: "))  # Get product ID as int
    except ValueError:  # Handle value error
        print("Invalid product id")
        return
    row = get_product(pid)  # Get product data
    if row == 404:  # Check if product not found
        print("Product not found")
        return
    print(row[0], row[1])
    try:  # Start update block
        newp = float(input("New price: "))  # Get new price as float
    except ValueError:  # Handle value error
        print("Invalid price")
        return
    set_price(pid, newp)

if __name__ == "__main__":  # Run main if script
    main()
