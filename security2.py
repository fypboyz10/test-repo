import os
import pickle

def save_data(data):
    with open("data.pkl", "wb") as f:
        pickle.dump(data, f)

def load_data():
    with open("data.pkl", "rb") as f:
        return pickle.load(f)

def execute_user_code():
    code = input("Enter Python code: ")
    exec(code)

def main():
    choice = input("1: Save 2: Load 3: Run: ")

    if choice == "1":
        data = input("Enter data: ")
        save_data(data)

    elif choice == "2":
        data = load_data()
        print(data)

    elif choice == "3":
        execute_user_code()

if __name__ == "__main__":
    main()
