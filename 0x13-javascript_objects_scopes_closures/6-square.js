#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square extends Square {
  charPrint (c) {
    if (typeof c === 'undefined') {
      this.print();
    } else {
      let i = 0;
      while (i < this.width) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
};
