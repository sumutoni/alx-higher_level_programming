#!/usr/bin/node

const process = require('process');
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

function add (a, b) {
  const res = a + b;
  console.log(res);
}
add(num1, num2);
