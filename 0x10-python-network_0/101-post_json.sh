#!/bin/bash
# post request of json file
curl -sL -H "Content-Type: application/json" -d @"$2" -X POST "$1"
