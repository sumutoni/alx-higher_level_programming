#!/usr/bin/node
const list = require('./100-data').list;
let newList = [];
let i = 0;
newList = list.map(y => y * i++);
console.log(list);
console.log(newList);
