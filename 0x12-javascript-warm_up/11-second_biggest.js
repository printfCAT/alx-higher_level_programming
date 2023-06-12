#!/usr/bin/node
const { argv } = require('process');
let bigone = 0;
let bigtwo = 0;
if (argv[2] === undefined || argv.length === 2) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    const current = argv[i];
    if (current > bigone) {
      bigtwo = bigone;
      bigone = current;
    } else if (current > bigtwo && current < bigone) {
      bigtwo = current;
    }
  }
  console.log(bigtwo);
}
