#!/bin/bash
# Script to displays all HTTP methods the server will accept
curl -s -I "$1" | grep "Allow" | cut -d " " -f 2-
