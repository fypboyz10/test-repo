import pickle

def load_user_preferences(serialized_data):
    return pickle.loads(serialized_data)


if __name__ == "__main__":
    user_input = input("Paste your saved session data: ").encode()
    preferences = load_user_preferences(user_input)
    print(preferences)
