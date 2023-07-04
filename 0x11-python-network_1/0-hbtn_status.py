#!/usr/bin/python3
""" define a python script """


import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print(response.read())
