#!/usr/bin/node
const fs = require('fs');
let data1 = '';
let data2 = '';
fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
fs.readFile(process.argv[3], 'utf8', (err, data) => {
  if (err) throw err;
  console.log(data);
});
fs.writeFile(process.argv[4], data1, (err) => {
  if (err) throw err;
});
fs.writeFile(process.argv[4], data2, (err) => {
  if (err) throw err;
});
