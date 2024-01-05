#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sIX ALLOW "$1" | grep allow: | tr -d ' ' | cut -d ':' -f2 | sed 's/,/, /g'
