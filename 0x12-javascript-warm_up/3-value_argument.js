#!/usr/bin/node
const numArguments = process.argv[2];
if (numArguments !== undefined) {
  console.log(numArguments);
} else {
  console.log('No argument');
}
