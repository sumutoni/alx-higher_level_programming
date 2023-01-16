#!/bin/bash
# get OPTIONS
curl -sLX OPTIONS "$1" | grep "Allow:" | cut -b8-
