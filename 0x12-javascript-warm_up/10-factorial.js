#!/usr/bin/node
function fact (a) {
  if (a === 1 || a === 0 || isNaN(a)) return 1;
  else return (a * fact(a - 1));
}
const proc = require('process');
console.log(fact(parseInt(proc.argv[2])));
