#!/usr/bin/python3
"""takes a user's GitHub credentials (username and password) and uses the
GitHub API to display a users id"""
import requests
import sys


if __name__ == "__main__":
    """uses a Github API to display a users id """
    repo = sys.argv[1]
    user = sys.argv[2]

    url = "https://api.github.com/repos/{}/{}/commits".format(user, repo)
    commits = requests.get(url).json()
    for i in range(10):
        if not isinstance(commits, list):
            continue
        author = commits[i].get('commit').get('author').get('name')
        sha = commits[i].get('sha')
        print("{}: {}".format(sha, author))
