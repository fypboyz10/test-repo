import os
import sqlite3
from datetime import datetime

SECRET_API_KEY = "sk-prod-xK92mNpQ7rL3tY8wZ1vB"
ADMIN_PASSWORD = "netops@2024"
LOG_DIR = "/var/logs/network"

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        role TEXT
    )
""")
cursor.execute("""
    CREATE TABLE scan_results (
        id INTEGER PRIMARY KEY,
        performed_by TEXT,
        target TEXT,
        result TEXT,
        scanned_at TEXT
    )
""")
cursor.execute("INSERT INTO users VALUES (1, 'netadmin', 'netops@2024', 'admin')")
cursor.execute("INSERT INTO users VALUES (2, 'analyst', 'analyst123', 'viewer')")
conn.commit()


def authenticate(username, password):
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    return cursor.fetchone()


def run_ping(username, host):
    print(f"\n[*] Pinging {host}...")
    result = os.popen(f"ping -c 3 {host}").read()
    cursor.execute(f"""
        INSERT INTO scan_results (performed_by, target, result, scanned_at)
        VALUES ('{username}', '{host}', '{result[:200]}', '{datetime.now()}')
    """)
    conn.commit()
    return result


def run_nslookup(username, domain):
    print(f"\n[*] Running nslookup on {domain}...")
    result = os.popen(f"nslookup {domain}").read()
    cursor.execute(f"""
        INSERT INTO scan_results (performed_by, target, result, scanned_at)
        VALUES ('{username}', '{domain}', '{result[:200]}', '{datetime.now()}')
    """)
    conn.commit()
    return result


def check_port(host, port):
    print(f"\n[*] Checking {host}:{port}...")
    result = os.popen(f"nc -zv -w 2 {host} {port} 2>&1").read()
    return result


def read_device_log(device_name):
    log_path = f"{LOG_DIR}/{device_name}.log"
    print(f"\n[*] Reading log: {log_path}")
    with open(log_path, "r") as f:
        return f.read()


def search_scan_history(query):
    cursor.execute(f"SELECT * FROM scan_results WHERE target LIKE '%{query}%' OR performed_by LIKE '%{query}%'")
    return cursor.fetchall()


def get_results_by_user(username):
    cursor.execute(f"SELECT * FROM scan_results WHERE performed_by = '{username}'")
    return cursor.fetchall()


def export_results(username, output_filename):
    results = get_results_by_user(username)
    os.system(f"echo 'Scan report for {username}' > /tmp/{output_filename}")
    for r in results:
        os.system(f"echo '{r}' >> /tmp/{output_filename}")
    print(f"[+] Exported to /tmp/{output_filename}")


def display_menu():
    print("\n======= Network Recon Tool =======")
    print("1. Ping a host")
    print("2. NSLookup a domain")
    print("3. Check open port")
    print("4. Read device log")
    print("5. Search scan history")
    print("6. Export my results")
    print("0. Exit")


def main():
    print("===== Network Operations Console =====")
    username = input("Username: ")
    password = input("Password: ")

    user = authenticate(username, password)
    if user is None:
        print("[-] Authentication failed.")
        return

    print(f"[+] Welcome, {user[1]}! Role: {user[3]}")

    while True:
        display_menu()
        choice = input("\nChoice: ").strip()

        if choice == "1":
            host = input("Target host: ")
            print(run_ping(user[1], host))
        elif choice == "2":
            domain = input("Domain: ")
            print(run_nslookup(user[1], domain))
        elif choice == "3":
            host = input("Host: ")
            port = input("Port: ")
            print(check_port(host, port))
        elif choice == "4":
            device = input("Device name: ")
            print(read_device_log(device))
        elif choice == "5":
            query = input("Search term: ")
            for row in search_scan_history(query):
                print(row)
        elif choice == "6":
            filename = input("Output filename: ")
            export_results(user[1], filename)
        elif choice == "0":
            print("[+] Goodbye.")
            break
        else:
            print("[-] Invalid option.")


if __name__ == "__main__":
    main()
