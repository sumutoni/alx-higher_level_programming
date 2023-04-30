#!/bin/bash
# post request of json file
curl -sLd @"$2" -X POST "$1"
