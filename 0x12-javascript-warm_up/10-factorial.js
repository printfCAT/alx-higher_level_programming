#!/usr/bin/node
function factorial (n) {
  if (n <= 1) {
    return 1;
  }
  return (n * factorial(n - 1));
}
const { argv } = require('process');
const n = parseInt(argv[2], 10);
if (isNaN(n)) {
  console.log(1);
} else {
  console.log(factorial(n));
}
