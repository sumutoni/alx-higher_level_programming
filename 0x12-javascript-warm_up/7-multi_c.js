#!/usr/bin/node

const process = require('process');

const num = Number(process.argv[2]);

if (isNaN(num)) console.log('Missing number of occurences');
else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
