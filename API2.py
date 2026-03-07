import requests

API_KEY = "sk_live_123456789SECRETKEY"

def get_data():
    url = "https://api.example.com/data"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)
    print(response.json())

get_data()
