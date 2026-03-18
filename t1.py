import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (username TEXT, password TEXT, balance INTEGER)")
cursor.execute("INSERT INTO users VALUES ('admin', '1234', 1000)")
conn.commit()

def login(username, password):
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    return cursor.fetchone()

def transfer_money(user, amount):
    cursor.execute("UPDATE users SET balance = balance - ? WHERE username = ?", (amount, user))
    conn.commit()
    print("Transfer completed")

def show_balance(user):
    query = "SELECT balance FROM users WHERE username = ?"
    cursor.execute(query, (user,))
    result = cursor.fetchone()
    if result is None:
        print("User not found")
    else:
        print("Balance:", result[0])

def main():
    username = input("Username: ")
    password = input("Password: ")
    user = login(username, password)
    if user is None:
        print("Login successful!")
    else:
        print("Login failed!")

    try:
        amt = int(input("Enter amount to transfer: "))
    except ValueError:
        print("Invalid amount")
        return

    transfer_money(username, amt)
    show_balance(username)

if __name__ == "__main__":
    main()
