#!/usr/bin/node
const { argv } = require('process');
const input = parseInt(argv[2], 10);
if (input === parseInt(argv[2], 10)) {
  console.log('My number:', argv[2]);
} else {
  console.log('Not a number');
}
