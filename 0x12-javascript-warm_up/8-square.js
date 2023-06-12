#!/usr/bin/node
const { argv } = require('process');
const num = parseInt(argv[2], 10);
if (num === parseInt(argv[2], 10)) {
  for (let i = 0; i < num; i++) {
    let row = '';
    for (let j = 0; j < num; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
