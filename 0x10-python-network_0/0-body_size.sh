#!/bin/bash
# send request to URL and display size of response body
curl -sI "$1" | grep "Content-Length" |cut -d ' ' -f2
