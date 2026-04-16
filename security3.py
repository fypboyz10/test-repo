import subprocess
import requests

def fetch_data(url):
    response = requests.get(url)
    return response.text

def run_command(cmd):
    subprocess.call(cmd, shell=True)

def main():
    url = input("Enter URL: ")
    data = fetch_data(url)

    filename = input("Enter file to save: ")
    with open(filename, "w") as f:
        f.write(data)

    command = input("Enter command to execute: ")
    run_command(command)

    print("Done")

if __name__ == "__main__":
    main()
