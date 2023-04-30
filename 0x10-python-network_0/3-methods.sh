#!/bin/bash
# display http methods server accepts
curl -sLX OPTIONS "$1"|grep "Allow:"|cut -b8-
