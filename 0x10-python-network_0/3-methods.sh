#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept curl -s -I -LX ALLOW "$1" | grep "allow:" | cut -d ' ' -f2-
curl -sIL -X ALLOW "$1" | grep "allow:" | cut -d ' ' -f 2-
