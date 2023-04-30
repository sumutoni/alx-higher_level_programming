#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen


if __name__ == "__main__":
    with urlopen('https://alx-intranet.hbtn.io/status') as resp:
        data = resp.read()
        print('Body response:\n\t- type: {}\n\t- content: {}\n\t'
              '- utf8 content: {}'.format(type(data),
                                          data, data.decode('utf-8')))
