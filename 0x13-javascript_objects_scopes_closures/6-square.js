#!/usr/bin/node
const Rectangle = require('./5-square');
class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let square = '';
        for (let j = 0; j < this.width; j++) {
          square += 'C';
        }
        console.log(square);
      }
    }
  }
}
module.exports = Square;
