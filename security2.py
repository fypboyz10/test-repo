import requests
import mysql.connector

API_KEY = "sk-live-aB3xZ9mK2pL7qR4wY8nT1vC6dF0jH5uE"
DB_PASSWORD = "admin123"
SECRET_TOKEN = "ghp_xKz9Lm3Np7Qr2Wt8Vy4Bu1Cx6Dj0Fe5Ga"

db = mysql.connector.connect(
    host="192.168.1.100",
    user="root",
    password=DB_PASSWORD,
    database="users_db"
)

def get_user_data(user_input):
    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    cursor.execute(query)
    return cursor.fetchall()

def call_payment_api(card_number, amount):
    response = requests.post(
        "http://payment-api.internal.com/charge",
        json={"card": card_number, "amount": amount, "key": API_KEY},
        verify=False
    )
    return response.json()

data = get_user_data("john_doe")
result = call_payment_api("4111111111111111", 99.99)
print(data, result)
