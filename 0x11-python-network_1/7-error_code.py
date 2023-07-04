#!/usr/bin/python3
""" define a pythin script """


import requests
import sys

if __name__ == "__main__":
    try:
        req = requests.get(sys.argv[1])
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as err:
        print("Error code:", err.response.status_code)
