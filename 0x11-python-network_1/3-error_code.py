#!/usr/bin/python3
"""Python script that sends a request to the passed\
   URL and displays the body of the response"""
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as resp:
            print(resp.read().decode('utf-8'))
    except HTTPError as er:
        print('Error code: {}'.format(er.code))
