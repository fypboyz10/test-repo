import requests

API_KEY = "sk_live_51JHk8dfh3k2j4h23kjh4k23jh4k2jh4"
BASE_URL = "https://api.example.com/data"

def fetch_data():
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(BASE_URL, headers=headers)
    return response.json()


if __name__ == "__main__":
    data = fetch_data()
    print(data)
