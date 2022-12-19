#!/usr/bin/node

const process = require('process');
const ar = [];
let j = 0;
for (let i = 2; i < process.argv.length; i++) {
  ar[j] = Number(process.argv[i]);
  j++;
}
let biggest = ar[0];
let ind = 0;
for (let i = 1; i < ar.length; i++) {
  if (biggest < ar[i]) {
    biggest = ar[i];
    ind = i;
  }
}
ar[ind] = 0;
let second = ar[0];
for (let i = 0; i < ar.length; i++) {
  if (second < ar[i]) second = ar[i];
}
console.log(second);
