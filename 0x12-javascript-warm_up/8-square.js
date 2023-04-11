#!/usr/bin/node
const proc = require('process');
const num = parseInt(proc.argv[2]);
if (!(isNaN(num))) {
  let i = 0;
  while (i < num) {
    console.log('X'.repeat(num));
    i = i + 1;
  }
} else console.log('Missing size');
