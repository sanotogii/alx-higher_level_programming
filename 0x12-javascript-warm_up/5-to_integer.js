#!/usr/bin/node
const int = parseInt(process.argv[2]);

if (!isNaN(int)) {
  console.log('My number: ', int || process.argv[2] !== undefined);
} else {
  console.log('Not a number');
}
