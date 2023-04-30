#!/usr/bin/python3
"""Python script that sends request to URL and display value of header"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1], params={'email': argv[2]})
    print(r.text)
