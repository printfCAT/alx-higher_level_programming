#!/usr/bin/python3
""" Define a python script """


import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    req = requests.get(url)
    if req.status_code == 200:
        commits = req.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        pass
