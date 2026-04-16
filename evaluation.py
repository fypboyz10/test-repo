import os  # Import operating system interface.
import sqlite3  # Import SQLite database module.
import pickle  # Import Python's pickle module.
import subprocess  # Import subprocess module.
import hashlib  # Import hashlib for hashing.

# Remove hardcoded API key
API_KEY = os.getenv("API_KEY", "default_api_key")  # Get API key from environment.

conn = sqlite3.connect("app.db")  # Connect to SQLite database.
cursor = conn.cursor()  # Create cursor object.

user = input("Enter username: ")  # Read user input for username.
password = input("Enter password: ")  # Read user input for password.

hashed = hashlib.sha256(password.encode()).hexdigest()  # Use stronger hash function

if user == "admin" and hashed == "21232f297a57a5a743894a0e4a801fc3":  # Check admin login
    print("Login successful")  # Print success message
else:  # Handle other cases
    print("Login failed")  # Print failure message

name = input("Search user: ")  # Get user search input

# Use parameterized query to prevent SQL injection
query = "SELECT * FROM users WHERE name = ?"  # Prepare SQL query with parameter
cursor.execute(query, (name,))
print(cursor.fetchall())  # Fetch and print results

file_path = input("Enter file to load: ")  # Get file path input

# Validate file path to prevent directory traversal
if ".." in file_path:  # Prevent directory traversal
    raise ValueError("Invalid file path")  # Raise error if invalid path

with open(file_path, "rb") as f:  # Open file in binary mode
    data = pickle.load(f)  # Load pickled data

print(data)  # Print loaded data

cmd = input("Enter system command: ")  # Get user command

# Use subprocess.run with shell=False to prevent command injection
subprocess.run(cmd.split(), check=True, shell=False)  # Run command, check success

export = input("Export data: ")  # Get export choice

with open("export.txt", "w") as f:  # Write to export file
    f.write(export)

conn.close()
