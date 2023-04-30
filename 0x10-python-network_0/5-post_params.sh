#!/bin/bash
# send post request
curl -sLd "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" -X POST "$1"
