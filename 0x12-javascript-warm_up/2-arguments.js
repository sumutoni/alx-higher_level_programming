#!/usr/bin/node
const proc = require('process');
if (proc.argv.length === 2) console.log('No argument');
else if (proc.argv.length === 3) console.log('Argument found');
else console.log('Arguments found');
