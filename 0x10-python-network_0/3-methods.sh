#!/bin/bash
# display http methods server accepts
curl -siLX OPTIONS "$1"|grep "Allow:"|cut -b8-
