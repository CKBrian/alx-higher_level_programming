#!/usr/bin/python3
"""Defines a module that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
import requests
import sys


if __name__ == "__main__":
    """ takes in a URL, sends a request to the URL and
    displays the body of the response"""
    url = sys.argv[1]
    resp = requests.get(url)
    code = resp.status_code

    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(resp.text)
