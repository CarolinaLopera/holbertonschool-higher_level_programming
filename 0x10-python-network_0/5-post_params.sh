#!/bin/bash
# Script to send a header variable to a URL.
curl -s -F email=test@gmail.com -F subject="I will always be here for PLD" "$1"
