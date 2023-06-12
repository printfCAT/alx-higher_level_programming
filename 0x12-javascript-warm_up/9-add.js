#!/usr/bin/node
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    return a + b;
  }
}
const { argv } = require('process');
const a = parseInt(argv[2], 10);
const b = parseInt(argv[3], 10);
console.log(add(a, b));
