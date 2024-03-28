#!/bin/bash
# This script takes a URL as an argument
curl -s -w "%{size_download}"  -o /dev/null "$1"