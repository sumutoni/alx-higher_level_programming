#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
