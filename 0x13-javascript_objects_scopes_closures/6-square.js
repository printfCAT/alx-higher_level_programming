#!/usr/bin/node
const Rectangle = require('./5-square');
module.exports = class Square extends Rectangle {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      let square = '';
      for (let j = 0; j < this.width; j++) {
        if (c === undefined) {
          square += 'X';
        } else {
          square += 'C';
        }
      }
      console.log(square);
    }
  }
};
