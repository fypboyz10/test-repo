import sqlite3

def get_user_by_username(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result


# Simulated usage
user_input = input("Enter username: ")
users = get_user_by_username(user_input)
print(users)
