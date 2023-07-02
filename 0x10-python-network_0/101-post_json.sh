#!/bin/bash
# sends a POST request with contents of a file
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
