#!/bin/bash
# get status code
curl -sL -w "%{http_code}" -o /dev/null "$1"
