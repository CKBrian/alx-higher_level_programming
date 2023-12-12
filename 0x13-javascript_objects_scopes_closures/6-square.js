#!/usr/bin/node

const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
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
