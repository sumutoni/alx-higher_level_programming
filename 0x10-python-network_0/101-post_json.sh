#!/bin/bash
# send POST request using file content
curl -sLd @"$2" -X POST "$1"
