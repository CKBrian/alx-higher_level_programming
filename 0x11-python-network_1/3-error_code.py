#!/usr/bin/python3
"""Defines a module that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
from urllib import request
from urllib import error
import sys


if __name__ == "__main__":
    """ takes in a URL, sends a request to the URL and
    displays the body of the response"""
    url = sys.argv[1]
    try:
        with request.urlopen(url) as resp:
            html = resp.read().decode("utf-8")
            print(html)
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
