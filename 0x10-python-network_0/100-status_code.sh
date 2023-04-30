#!/bin/bash
# get status code
curl -sL -w "%{http_code}" "$1"
