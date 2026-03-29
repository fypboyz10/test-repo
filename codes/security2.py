import sqlite3
import json
import base64
import hashlib
from datetime import datetime

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT,
        email TEXT, role TEXT DEFAULT 'user', credit_card TEXT, balance REAL DEFAULT 0.0
    )
""")
cursor.execute("""
    CREATE TABLE transactions (
        id INTEGER PRIMARY KEY, sender_id INTEGER, receiver_id INTEGER,
        amount REAL, note TEXT, created_at TEXT
    )
""")
cursor.execute("INSERT INTO users VALUES (1, 'alice', 'alice123', 'alice@bank.com', 'user', '4111111111111111', 2500.0)")
cursor.execute("INSERT INTO users VALUES (2, 'bob', 'bob456', 'bob@bank.com', 'user', '4222222222222222', 800.0)")
cursor.execute("INSERT INTO users VALUES (3, 'bankadmin', 'adm!n99', 'admin@bank.com', 'admin', '4333333333333333', 0.0)")
cursor.execute("INSERT INTO transactions VALUES (1, 1, 2, 200.0, 'Rent split', '2024-01-10 09:00:00')")
conn.commit()


def create_token(user_id, username, role):
    payload = {"user_id": user_id, "username": username, "role": role}
    return base64.b64encode(json.dumps(payload).encode()).decode()


def decode_token(token):
    return json.loads(base64.b64decode(token.encode()).decode())


def login(username, password):
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    user = cursor.fetchone()
    if user:
        token = create_token(user[0], user[1], user[4])
        print(f"[+] Logged in as {username}. Token: {token}")
        return user, token
    print("[-] Login failed.")
    return None, None


def register(username, password, email, extra_fields=None):
    fields = {"username": username, "password": hashlib.md5(password.encode()).hexdigest(), "email": email, "role": "user"}
    if extra_fields:
        fields.update(extra_fields)
    cols = ", ".join(fields.keys())
    vals = ", ".join([f"'{v}'" for v in fields.values()])
    cursor.execute(f"INSERT INTO users ({cols}) VALUES ({vals})")
    conn.commit()
    print(f"[+] Registered {username}")


def get_profile(target_user_id):
    cursor.execute(f"SELECT id, username, email, role, credit_card, balance FROM users WHERE id = {target_user_id}")
    u = cursor.fetchone()
    if u:
        print(f"\n  Username: {u[1]} | Email: {u[2]} | Role: {u[3]} | Card: {u[4]} | Balance: ${u[5]:.2f}")


def update_profile(target_user_id, field, value):
    cursor.execute(f"UPDATE users SET {field} = '{value}' WHERE id = {target_user_id}")
    conn.commit()
    print(f"[+] Updated '{field}' for user {target_user_id}")


def transfer_funds(token, receiver_id, amount, note):
    claims = decode_token(token)
    cursor.execute(f"SELECT balance FROM users WHERE id = {claims['user_id']}")
    balance = cursor.fetchone()[0]
    if balance < amount:
        print("[-] Insufficient balance.")
        return
    cursor.execute(f"UPDATE users SET balance = balance - {amount} WHERE id = {claims['user_id']}")
    cursor.execute(f"UPDATE users SET balance = balance + {amount} WHERE id = {receiver_id}")
    cursor.execute(f"""
        INSERT INTO transactions (sender_id, receiver_id, amount, note, created_at)
        VALUES ({claims['user_id']}, {receiver_id}, {amount}, '{note}', '{datetime.now()}')
    """)
    conn.commit()
    print(f"[+] Transferred ${amount:.2f} to user {receiver_id}")


def get_transaction(transaction_id):
    cursor.execute(f"SELECT * FROM transactions WHERE id = {transaction_id}")
    txn = cursor.fetchone()
    if txn:
        print(f"\n  From: {txn[1]} | To: {txn[2]} | Amount: ${txn[3]:.2f} | Note: {txn[4]}")


def admin_list_users(token):
    claims = decode_token(token)
    if claims.get("role") == "admin":
        cursor.execute("SELECT id, username, email, role, credit_card, password, balance FROM users")
        print("\n[=== ALL USERS ===]")
        for u in cursor.fetchall():
            print(f"  {u}")


def display_menu():
    print("\n======= Banking Portal =======")
    print("1. View profile (by ID)  2. Update profile field")
    print("3. Transfer funds        4. View transaction (by ID)")
    print("5. Admin: list users     0. Logout")


def main():
    print("===== SecureBank Portal =====")
    print("1. Login  2. Register")
    choice = input("Choice: ").strip()

    if choice == "2":
        username = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")
        extra_raw = input("Extra fields as JSON (or leave blank): ").strip()
        extra = json.loads(extra_raw) if extra_raw else {}
        register(username, password, email, extra)
        return

    username = input("Username: ")
    password = input("Password: ")
    user, token = login(username, password)
    if not user:
        return

    while True:
        display_menu()
        opt = input("\nChoice: ").strip()
        if opt == "1":
            get_profile(input("User ID: "))
        elif opt == "2":
            update_profile(input("User ID: "), input("Field: "), input("Value: "))
        elif opt == "3":
            transfer_funds(token, int(input("Receiver ID: ")), float(input("Amount: ")), input("Note: "))
        elif opt == "4":
            get_transaction(input("Transaction ID: "))
        elif opt == "5":
            admin_list_users(input("Provide token: "))
        elif opt == "0":
            print("[+] Logged out.")
            break


if __name__ == "__main__":
    main()
