#!/usr/bin/node
const arg = process.argv[2];
const int = parseInt(arg);

if (!isNaN(int)) {
  console.log('My number: ', int || process.argv[2] !== undefined);
} else {
  console.log('Not a number');
}
