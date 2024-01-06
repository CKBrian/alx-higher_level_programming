#!/usr/bin/python3
"""Defines a module that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)."""
import requests
from requests.exceptions import HTTPError
import sys


if __name__ == "__main__":
    """ takes in a URL, sends a request to the URL and
    displays the body of the response"""
    url = sys.argv[1]
    try:
        resp = requests.get(url)
        print(resp.text)
    except HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
