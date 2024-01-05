#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept.
curl -sILX ALLOW "$1" | grep "allow:" | cut -d ' ' -f2-
