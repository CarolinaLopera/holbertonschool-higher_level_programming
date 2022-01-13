#!/bin/bash
# Script to takes in a URL, sends a DELETE request and displays the response.
curl -sX DELETE "$1"
