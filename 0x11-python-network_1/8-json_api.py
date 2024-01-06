#!/usr/bin/python3
""" defines a module that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter."""
import requests
import sys


def request_url(letter=""):
    """takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter  """
    try:
        url = http://0.0.0.0:5000/search_user
        params = {'q': letter}
        resp = requests.post(url, params)
        if len(resp.headers) == 0:
            print("No result")
        else:
            print("[{}] {}".format(resp.get('id'), resp.get('name')))
    except ValueError:
        print(" Not a valid JSON")


if __name__ == "__main__":
    if (sys.argv[1]):
        request_url(sys.argv[1])
    else:
        request_url()
