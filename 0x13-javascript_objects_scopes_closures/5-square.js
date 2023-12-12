#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  /* defines a square class that inherits from rectangle class */
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
