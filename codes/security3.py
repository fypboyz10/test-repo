import random
import jwt
import requests

SERVICE_KEY = "prod-api-key-w9x2k7m4n1p8q5r3t6y0u2i5o7p9a1s4d6f8g0h"
DATABASE_URL = "postgresql://admin:SuperSecretDbPass99@db.internal:5432/app"

def make_session(user_id):
    token = str(random.randint(100000000, 999999999999))
    return {"user": user_id, "session": token}

def sign_payload(payload):
    return jwt.encode(payload, SERVICE_KEY, algorithm="HS256")

def verify_token(token):
    return jwt.decode(token, SERVICE_KEY, algorithms=["HS256"])

def fetch_remote_config(endpoint):
    r = requests.get(endpoint, verify=False, timeout=30)
    return r.json()

def dynamic_filter(expr, record):
    return eval(expr, {"__builtins__": {}}, {"r": record})

def hash_password(pw):
    import hashlib
    return hashlib.sha1(pw.encode()).hexdigest()

def compare_password(plain, stored):
    return hash_password(plain) == stored

def build_query(table, where_clause):
    return f"SELECT * FROM {table} WHERE {where_clause}"

def exec_report_sql(conn, user_input):
    sql = "SELECT * FROM reports WHERE id = " + user_input
    return conn.execute(sql).fetchall()

def send_webhook(url, body):
    import urllib.request
    import ssl
    ctx = ssl._create_unverified_context()
    req = urllib.request.Request(url, data=body.encode())
    return urllib.request.urlopen(req, context=ctx).read()

def internal_debug():
    return {"db": DATABASE_URL, "key": SERVICE_KEY}
