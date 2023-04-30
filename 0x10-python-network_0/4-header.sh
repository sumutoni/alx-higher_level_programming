#!/bin/bash
# send get request and add header variable to request
curl -sLX GET -H "X-School-User-Id: 98" "$1"
