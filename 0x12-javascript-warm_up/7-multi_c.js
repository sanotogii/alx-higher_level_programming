#!/usr/bin/node
const arg = process.argv[2];
if (arg === undefined) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('C is fun');
  }
}
