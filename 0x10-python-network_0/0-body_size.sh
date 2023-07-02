#!/bin/bash
# displays the size in bytes for a given URL 
curl -s "$1" | wc -c
