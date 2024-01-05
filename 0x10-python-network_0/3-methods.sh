#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sI ALLOW "$1" -L | grep allow: | tr -d ' ' | cut -d ':' -f2 | sed 's/,/, /g'
