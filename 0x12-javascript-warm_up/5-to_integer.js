#!/usr/bin/node
const arg = Number(process.argv[2]);
if (Number.isNaN(arg) || arg === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ', arg);
}
