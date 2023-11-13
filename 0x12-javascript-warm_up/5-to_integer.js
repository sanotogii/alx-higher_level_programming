#!/usr/bin/node
const int = process.argv[2];

if (!isNaN(int) || process.argv[2] !== undefined) {
  console.log('My number: ', int);
} else {
  console.log('Not a number');
}
