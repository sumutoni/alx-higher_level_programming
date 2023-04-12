#!/usr/bin/node
const dict = require('./101-data').dict;
function reverse () {
  const newDict = {};
  const values = Object.values(dict);
  function newdict () {
    for (let i = 0; i < values.length; i++) {
      const keyArray = [];
      for (const k in dict) {
        if (dict[k] === values[i] && !(Object.values(newDict).includes(values[i]))) {
          keyArray.push(k);
        }
      }
      newDict[values[i]] = keyArray;
    }
  }
  newdict();
  console.log(newDict);
}
reverse();
