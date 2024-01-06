#!/usr/bin/python3
"""Defines a module that  takes in a URL and an email, sends a POST request to
the passed URL with the email as a parameter, and displays the body of the
response"""
import requests
from urllib import parse
import sys


if __name__ == "__main__":
    """takes in a URL and an email, sends a POST request to
    the passed URL with the email as a parameter and displays the response"""
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    resp = requests.post(url, params)
    print()
