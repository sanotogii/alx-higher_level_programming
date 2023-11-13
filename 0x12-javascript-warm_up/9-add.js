#!/usr/bin/node
const arg1 = process.argv[2];
const arg2 = process.argv[3];
if (arg1 === undefined || arg2 === undefined) {
  console.log('NaN');
} else {
  const sum = Number(arg1) + Number(arg2);
  console.log(sum);
}
