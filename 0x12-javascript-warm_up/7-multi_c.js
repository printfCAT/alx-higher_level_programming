#!/usr/bin/node
const { argv } = require('process');
const word = 'C is fun';
const num = parseInt(argv[2], 10);
if (num === parseInt(argv[2], 10)) {
  let i = 0;
  while (i < num) {
    console.log(word);
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
