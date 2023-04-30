#!/usr/bin/python3
"""Python script that sends post request to URL with letter as parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) == 1:
        r = requests.post(url, data={'q': ''})
    else:
        r = requests.post(url, data={'q': argv[1]})
    try:
        cont = r.json()
    except ValueError as e:
        print('Not a valid JSON')
    if not cont:
        print('No result')
    else:
        print('[{}] {}'.format(cont.get('id'), cont.get('name')))
