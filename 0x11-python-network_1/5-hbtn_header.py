#!/usr/bin/python3
""" define a python script """


import requests
import sys

if __name__ == "__main__":
    req = requests.get(sys.argv[1])
    print(req.headers.get('X-Request-Id'))
