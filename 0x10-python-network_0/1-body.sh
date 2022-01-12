#!/bin/bash
# Script to takes in a URL, sends a GET request and displays the body of the response.
res=$(curl -sw '%{http_code}' -o /dev/null "$1"); [[ res -eq 200 ]] && curl -sX GET "$1"
