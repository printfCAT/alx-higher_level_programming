#!/usr/bin/python3
""" define a python script """


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No result")
    else:
        letter = sys.argv[1]
        req = requests.post('http://0.0.0.0:5000/search_user',
                            data={'q': letter})
        try:
            json_data = req.json()
            if json_data:
                print("[{}] {}".format(json_data.get('id'),
                                       json_data.get('name')))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
