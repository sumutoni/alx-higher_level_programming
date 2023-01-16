#!/bin/bash
# send GET request with a header
curl -sL -H "X-School-User-Id: 98" -X GET "$1"
