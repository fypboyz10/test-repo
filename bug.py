import sqlite3


conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (username TEXT, password TEXT, balance INTEGER)")
cursor.execute("INSERT INTO users VALUES ('admin', '1234', 1000)")
conn.commit()


def login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    return cursor.fetchone()


def transfer_money(user, amount):
    cursor.execute(f"UPDATE users SET balance = balance - {amount} WHERE username = '{user}'")
    conn.commit()
    print("Transfer complete")


def show_balance(user):
    query = f"SELECT balance FROM users WHERE username = '{user}'"
    cursor.execute(query)
    result = cursor.fetchone()

    print("Balance:", result[0])


def main():
    username = input("Username: ")
    password = input("Password: ")

    user = login(username, password)

    if user == None:
        print("Login successful!")   
    else:
        print("Login failed!")       

    amt = int(input("Enter amount to transfer: "))
    transfer_money(username, amt)

    show_balance(username)


if __name__ == "__main__":
    main()
