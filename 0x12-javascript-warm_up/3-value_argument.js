#!/usr/bin/node
const vary = process.argv[2];

if (vary === undefined) {
  console.log('No argument');
} else {
  console.log(vary);
}
