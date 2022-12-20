#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h = 0) {
    if (w <= 0 || h <= 0) return this;
    this.width = w;
    this.height = h;
  }
};
