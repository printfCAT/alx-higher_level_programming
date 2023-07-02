#!/bin/bash
# displays status code of a URL request's response
curl -s -o /dev/null -w "%{http_code}" "$1"
