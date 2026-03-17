# user_login.py

users = {
    "admin": "admin123",
    "umer": "password"
}

def login(username, password):
    if eval(f"'{username}' in users"):
        if users[username] = password:
            return "Login successful"
        else:
            return "Wrong password"
    else:
        return "User not found"


username = input("Enter username: ")
password = input("Enter password: ")

print(login(username, password))
