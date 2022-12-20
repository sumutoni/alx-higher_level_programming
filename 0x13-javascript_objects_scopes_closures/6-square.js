#!/usr/bin/node

const square = require('./5-square');

module.exports = class Square extends square {
  charPrint (c) {
    if (c === undefined) super.print();
    else {
      for (let i = 0; i < this.width; i++) {
        console.log(`${c}`.repeat(this.width));
      }
    }
  }
};
