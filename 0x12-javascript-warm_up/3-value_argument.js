#!/usr/bin/node
const { argv } = require('process');
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  let i = 2;
  while (argv[i] !== undefined) {
    console.log(argv[i]);
    i++;
  }
}
