#!/bin/bash
# sends a POST request with contents of a file
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1"
