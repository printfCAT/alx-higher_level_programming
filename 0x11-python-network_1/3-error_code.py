#!/usr/bin/python3
""" define a python script """


import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read()
        print(page.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
