#!/usr/bin/node

const process = require('process');
const num = Number(process.argv[2]);

if (isNaN(num)) console.log('Not a number');
else console.log(num);
