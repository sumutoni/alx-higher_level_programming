#!/usr/bin/node
const proc = require('process');
const num = parseInt(proc.argv[2]);
if (!(isNaN(num))) console.log('My number: ' + num);
else console.log('Not a number');
