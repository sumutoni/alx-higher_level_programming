#!/usr/bin/node

const process = require('process');
const num = Number(process.argv[2]);

function fact (x) {
  if (x === 1) return 1;
  else {
    x = x * fact(x - 1);
  }
  return x;
}
if (isNaN(num)) console.log('1');
else console.log(fact(num));
