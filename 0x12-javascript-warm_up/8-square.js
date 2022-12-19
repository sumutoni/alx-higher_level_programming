#!/usr/bin/node

const process = require('process');

const num = Number(process.argv[2]);

if (isNaN(num)) console.log('Missing size');
else {
  for (let i = 0; i < num; i++) {
    console.log('X'.repeat(num));
  }
}
