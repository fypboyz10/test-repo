import requests

API_KEY = "sk-1234567890abcdefSECRETKEY"
API_URL = "https://api.example.com/data"

def get_data():
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.get(API_URL, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error:", response.status_code)

data = get_data()
print(data)
