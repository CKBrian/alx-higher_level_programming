#!/usr/bin/python3
"""takes a user's GitHub credentials (username and password) and uses the
GitHub API to display a users id"""
import requests
import sys


if __name__ == "__main__":
    """uses a Github API to display a users id """
    user = sys.argv[1]
    passwd = sys.argv[2]
    url = "https://api.github.com/user"
    resp = requests.get(url, auth=(user, passwd)).json()
    print("{}".format(resp.get('id')))
