#!/bin/bash
# displays status code of a URL request's response
curl -s -w "%{http_code}" "$1"
