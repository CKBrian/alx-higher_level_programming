#!/usr/bin/python3
"""Defines a module that  fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    """ fetches https://alx-intranet.hbtn.io/status"""
    html = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(html.text)))
    print("\t- content: {}".format(html.text))
