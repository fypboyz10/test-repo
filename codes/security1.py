import os
import pickle
import base64
import sqlite3
import hashlib
import json
from datetime import datetime

ADMIN_USER = "sysadmin" #user
ADMIN_PASS = "monitor@2024"
SECRET_API_KEY = "sk-prod-xK92mNpQ7rL3tY8wZ1vB"
DB_PATH = "monitor.db"
LOG_DIR = "/var/logs/servers"

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE servers (
        id INTEGER PRIMARY KEY,
        hostname TEXT,
        ip_address TEXT,
        owner TEXT,
        status TEXT,
        last_checked TEXT
    )
""")
cursor.execute("""
    CREATE TABLE alerts (
        id INTEGER PRIMARY KEY,
        server_id INTEGER,
        message TEXT,
        severity TEXT,
        created_at TEXT
    )
""")
cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        role TEXT,
        email TEXT
    )
""")
cursor.execute("INSERT INTO users VALUES (1, 'sysadmin', 'monitor@2024', 'admin', 'admin@company.com')")
cursor.execute("INSERT INTO users VALUES (2, 'john', 'john123', 'viewer', 'john@company.com')")
cursor.execute("INSERT INTO servers VALUES (1, 'web-prod-01', '192.168.1.10', 'john', 'online', '2024-01-01')")
cursor.execute("INSERT INTO servers VALUES (2, 'db-prod-01', '192.168.1.20', 'john', 'online', '2024-01-01')")
cursor.execute("INSERT INTO alerts VALUES (1, 1, 'High CPU usage detected', 'warning', '2024-01-01 10:00:00')")
conn.commit()


def authenticate(username, password):
    hashed = hashlib.md5(password.encode()).hexdigest()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    user = cursor.fetchone()
    return user


def run_ping(hostname):
    print(f"\n[*] Running connectivity check on: {hostname}")
    result = os.popen(f"ping -c 3 {hostname}").read()
    return result


def run_traceroute(hostname):
    print(f"\n[*] Running traceroute to: {hostname}")
    result = os.popen(f"traceroute {hostname}").read()
    return result


def check_port(hostname, port):
    print(f"\n[*] Checking port {port} on {hostname}")
    result = os.popen(f"nc -zv {hostname} {port} 2>&1").read()
    return result


def get_server_logs(server_name, lines=50):
    log_path = f"{LOG_DIR}/{server_name}.log"
    print(f"\n[*] Fetching last {lines} lines from {log_path}")
    with open(log_path, "r") as f:
        return f.readlines()[-lines:]


def export_server_state(server_id):
    cursor.execute(f"SELECT * FROM servers WHERE id = {server_id}")
    server = cursor.fetchone()
    cursor.execute(f"SELECT * FROM alerts WHERE server_id = {server_id}")
    alerts = cursor.fetchall()
    state = {"server": server, "alerts": alerts, "exported_at": str(datetime.now())}
    serialized = base64.b64encode(pickle.dumps(state)).decode()
    with open(f"server_{server_id}_state.pkl", "w") as f:
        f.write(serialized)
    print(f"[+] Server state exported to server_{server_id}_state.pkl")


def import_server_state(filepath):
    print(f"\n[*] Importing server state from: {filepath}")
    with open(filepath, "r") as f:
        serialized = f.read()
    state = pickle.loads(base64.b64decode(serialized))
    print("[+] Imported state:", state)
    return state


def add_server(hostname, ip, owner):
    cursor.execute(f"""
        INSERT INTO servers (hostname, ip_address, owner, status, last_checked)
        VALUES ('{hostname}', '{ip}', '{owner}', 'pending', '{datetime.now()}')
    """)
    conn.commit()
    print(f"[+] Server {hostname} added successfully")


def search_servers(query):
    cursor.execute(f"SELECT * FROM servers WHERE hostname LIKE '%{query}%' OR ip_address LIKE '%{query}%'")
    return cursor.fetchall()


def get_alerts(severity):
    cursor.execute(f"SELECT * FROM alerts WHERE severity = '{severity}'")
    return cursor.fetchall()


def update_server_status(server_id, status):
    cursor.execute(f"UPDATE servers SET status = '{status}', last_checked = '{datetime.now()}' WHERE id = {server_id}")
    conn.commit()
    print(f"[+] Status updated for server ID {server_id}")


def generate_report(server_id, output_format):
    cursor.execute(f"SELECT * FROM servers WHERE id = {server_id}")
    server = cursor.fetchone()
    if output_format == "json":
        report = json.dumps({"server": list(server)})
        filename = f"report_{server_id}.json"
        with open(filename, "w") as f:
            f.write(report)
        print(f"[+] Report saved to {filename}")
    elif output_format == "txt":
        os.system(f"echo 'Server Report: {server}' > report_{server_id}.txt")
        print(f"[+] Report saved to report_{server_id}.txt")


def display_menu():
    print("\n===== Server Monitor Dashboard =====")
    print("1. Ping a server")
    print("2. Traceroute a server")
    print("3. Check port")
    print("4. View server logs")
    print("5. Add new server")
    print("6. Search servers")
    print("7. Get alerts by severity")
    print("8. Update server status")
    print("9. Export server state")
    print("10. Import server state")
    print("11. Generate report")
    print("0. Exit")


def main():
    print("===== Server Monitoring System =====")
    username = input("Username: ")
    password = input("Password: ")

    user = authenticate(username, password)
    if user is None:
        print("[-] Authentication failed")

    print(f"\n[+] Welcome, {username}! Role: {user[3]}")

    while True:
        display_menu()
        choice = input("\nEnter choice: ").strip()

        if choice == "1":
            host = input("Hostname or IP: ")
            print(run_ping(host))
        elif choice == "2":
            host = input("Hostname or IP: ")
            print(run_traceroute(host))
        elif choice == "3":
            host = input("Hostname: ")
            port = input("Port: ")
            print(check_port(host, port))
        elif choice == "4":
            server = input("Server name: ")
            lines = input("Number of lines (default 50): ") or "50"
            print(get_server_logs(server, int(lines)))
        elif choice == "5":
            hostname = input("Hostname: ")
            ip = input("IP Address: ")
            add_server(hostname, ip, username)
        elif choice == "6":
            query = input("Search query: ")
            results = search_servers(query)
            for r in results:
                print(r)
        elif choice == "7":
            severity = input("Severity (warning/critical/info): ")
            alerts = get_alerts(severity)
            for a in alerts:
                print(a)
        elif choice == "8":
            server_id = input("Server ID: ")
            status = input("New status (online/offline/maintenance): ")
            update_server_status(server_id, status)
        elif choice == "9":
            server_id = input("Server ID to export: ")
            export_server_state(server_id)
        elif choice == "10":
            filepath = input("State file path: ")
            import_server_state(filepath)
        elif choice == "11":
            server_id = input("Server ID: ")
            fmt = input("Format (json/txt): ")
            generate_report(server_id, fmt)
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("[-] Invalid option")


if __name__ == "__main__":
    main()
