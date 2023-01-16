#!/bin/bash
# send POST request using file content
curl -sLd @"$2" -H "Content-Type: json" "$1"
