#!/usr/bin/python3
"""Python script that sends post request to URL with letter as parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://api.github.com/user'
    headers = {'Accept': 'application/vnd.github+json'}
    r = requests.get(url, headers=headers, auth=(argv[1], argv[2]))
    print(r.json().get('id'))
