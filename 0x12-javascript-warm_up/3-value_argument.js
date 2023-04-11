#!/usr/bin/node
const proc = require('process');
if (proc.argv[2]) console.log(proc.argv[2]);
else console.log('No argument');
