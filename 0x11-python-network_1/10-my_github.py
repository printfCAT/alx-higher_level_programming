#!/usr/bin/python3
""" Define a Python script """

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = f"https://api.github.com/users/{username}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        print(user_id if user_id else "None")
    else:
        print("None")
