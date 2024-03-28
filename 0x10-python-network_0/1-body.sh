#!/bin/bash
# cURL to the end
curl -sL -w "%{http_code}" "$1" -o /dev/null | grep -q "200" && curl -s "$URL"

