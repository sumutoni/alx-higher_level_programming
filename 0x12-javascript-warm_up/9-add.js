#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const proc = require('process');
add(parseInt(proc.argv[2]), parseInt(proc.argv[3]));
