#!/usr/bin/node
const arg = process.argv[2];
const int = parseInt(arg);

if (!isNaN(int)) {
  console.log('My number: ', int);
} else {
  console.log('Not a number');
}
