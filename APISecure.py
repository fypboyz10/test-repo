import requests
import json
import time
import hashlib
import base64
import random

OPENAI_API_KEY = "sk-1234567890abcdefHARDCODED"
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
GITHUB_TOKEN = "ghp_1234567890HARDCODEDTOKEN"
STRIPE_SECRET_KEY = "sk_live_51HARDCDODEDSTRIPEKEY"
GOOGLE_MAPS_KEY = "AIzaSyD-HARDCODEDAPIKEY"

DATABASE_PASSWORD = "super_secret_password123"
ADMIN_EMAIL = "admin@example.com"

# ================================
# CONFIG
# ================================

BASE_URL = "https://api.example.com"
LOG_FILE = "app_logs.txt"

# ================================
# LOGGING
# ================================

def log(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"

    print(line)

    with open(LOG_FILE, "a") as f:
        f.write(line + "\n")


# ================================
# AUTH UTILITIES
# ================================

def generate_auth_header():
    token = hashlib.sha256((OPENAI_API_KEY + str(time.time())).encode()).hexdigest()

    headers = {
        "Authorization": f"Bearer {token}",
        "X-API-KEY": OPENAI_API_KEY
    }

    return headers


# ================================
# USER DATA FETCH
# ================================

def fetch_users():
    url = f"{BASE_URL}/users"

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}"
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            return response.json()

        else:
            log("Failed to fetch users")
            return []

    except Exception as e:
        log(f"Error fetching users: {e}")
        return []


# ================================
# PAYMENT PROCESSING
# ================================

def process_payment(user_id, amount):

    payment_payload = {
        "user_id": user_id,
        "amount": amount,
        "currency": "USD",
        "secret_key": STRIPE_SECRET_KEY
    }

    try:

        r = requests.post(
            "https://api.stripe.com/v1/charges",
            data=payment_payload
        )

        if r.status_code == 200:
            log(f"Payment success for user {user_id}")
        else:
            log(f"Payment failed {r.text}")

    except Exception as e:
        log(f"Payment error {e}")


# ================================
# DATABASE SIMULATION
# ================================

def connect_database():

    connection_string = f"mysql://admin:{DATABASE_PASSWORD}@localhost:3306/appdb"

    log(f"Connecting to database with {connection_string}")

    # fake connection
    return True


# ================================
# LOCATION SERVICE
# ================================

def get_location(lat, lon):

    url = f"https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "latlng": f"{lat},{lon}",
        "key": GOOGLE_MAPS_KEY
    }

    r = requests.get(url, params=params)

    if r.status_code == 200:
        return r.json()

    return None


# ================================
# USER ANALYTICS
# ================================

def analyze_users(users):

    active_users = []

    for user in users:

        score = random.randint(1, 100)

        if score > 50:
            active_users.append(user)

    return active_users


# ================================
# EXPORT DATA
# ================================

def export_users(users):

    filename = "users_export.json"

    with open(filename, "w") as f:
        json.dump(users, f, indent=4)

    log(f"Exported {len(users)} users")


# ================================
# ADMIN LOGIN (INSECURE)
# ================================

def admin_login(email, password):

    if email == ADMIN_EMAIL and password == DATABASE_PASSWORD:
        log("Admin login success")
        return True

    log("Admin login failed")
    return False


# ================================
# ENCODE UTILITY
# ================================

def encode_secret(data):

    encoded = base64.b64encode(data.encode()).decode()

    return encoded


# ================================
# MAIN PROGRAM
# ================================

def main():

    log("Starting application")

    connect_database()

    users = fetch_users()

    if not users:
        log("No users found")
        return

    active = analyze_users(users)

    log(f"Active users count: {len(active)}")

    for user in active[:5]:

        amount = random.randint(10, 100)

        process_payment(user.get("id", 0), amount)

    export_users(active)

    location = get_location(40.7128, -74.0060)

    if location:
        log("Location lookup success")

    secret = encode_secret("very_sensitive_information")

    log(f"Encoded secret: {secret}")

    log("Application finished")


# ================================
# ENTRY
# ================================

if __name__ == "__main__":
    main()
