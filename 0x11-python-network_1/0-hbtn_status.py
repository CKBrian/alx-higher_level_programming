#!/usr/bin/python3
"""Defines a module that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request


if __name__ == "__main__":
    """fetches information from https://alx-intranet.hbtn.io/status"""
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.read()
        print("Body response:")
        print("    - type: {}".format(type(data)))
        print("    - content: {}".format(data))
        respn = data.decode("utf-8")
        print("    - utf8 content: {}".format(respn))
