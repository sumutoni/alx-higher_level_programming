#!/usr/bin/node
const proc = require('process');
if (proc.argv.length === 2 || proc.argv.length === 3) console.log('0');
else {
  let first = parseInt(proc.argv[2]);
  let second = 0;
  for (let i = 3; i < proc.argv.length; i++) {
    if (parseInt(proc.argv[i]) > first) {
      second = first;
      first = parseInt(proc.argv[i]);
    }
    if (parseInt(proc.argv[i]) < first && parseInt(proc.argv[i]) > second) {
      second = parseInt(proc.argv[i]);
    }
  }
  console.log(second);
}
