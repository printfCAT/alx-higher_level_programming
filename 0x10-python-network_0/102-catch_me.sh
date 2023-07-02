#!/bin/bash
# sends a request to a server that responds with a message
curl -s -X PUT -H "Origin: You got me!" 0.0.0.0:5000/catch_me
