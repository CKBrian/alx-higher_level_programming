#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  /* defines a square class that inherits from rectangle class */
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.height; i++) {
        console.log(String(c).repeat(this.width));
      }
    } else {
      super.print();
    }
  }
}

module.exports = Square;
