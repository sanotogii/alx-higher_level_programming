#!/bin/bash
# This script takes a URL as an argument, sends a request to that URL, and displays the size of the body of the response.

url=$1
curl -sI "$url" | grep 'Content-Length' | cut -d' ' -f2