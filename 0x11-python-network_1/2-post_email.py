#!/usr/bin/python3
"""Python script that sends a POST request to the passed URL\
   with the email as a parameter, and displays the body of the response"""
from urllib.request import urlopen, Request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    value = {'email': argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    url = Request(argv[1], data)
    with urlopen(url) as resp:
        print(resp.read().decode('utf-8'))
