#!/usr/bin/python3
""" define a python script """


import requests

if __name__ == "__main__":
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.content))
    print("\t- content:", req.content)
