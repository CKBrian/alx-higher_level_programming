#!/usr/bin/python3
"""Defines a module that sends a request to the URL and displays the value
of the `X-Request-Id` variable found in the header of the response."""
import requests
import sys


if __name__ == "__main__":
    """
    sends a request to the URL and displays the value
    of the X-Request-Id variable found in the header of the response."""
    url = sys.argv[1]
	resp = requests.get(url)
    print(resp.headers['X-Request-Id'])
