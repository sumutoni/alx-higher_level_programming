#!/bin/bash
# send POST request with variables
curl -sLd "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" -X POST "$1"
