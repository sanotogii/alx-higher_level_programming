#!/bin/bash
# This script takes a URL as an argument
curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2