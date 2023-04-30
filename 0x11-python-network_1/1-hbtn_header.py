#!/usr/bin/python3
"""Python script that sends request to URL and display value of header"""
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    with urlopen(argv[1]) as resp:
        print(resp.info().get('X-Request-Id'))
