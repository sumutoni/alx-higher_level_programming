#!/usr/bin/python3
"""Python script that sends request to URL and display value of header"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.post(argv[1], data={'email': argv[2]})
    print(r.text)
