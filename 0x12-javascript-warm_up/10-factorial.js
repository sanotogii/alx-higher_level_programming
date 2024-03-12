#!/usr/bin/node
const n = Number(process.argv[2]);
function fact (n) {
  if (n === 1 || n === 0 || Number.isNaN(n)) {
    return 1;
  } else {
    return n * fact(n - 1);
  }
}

console.log(fact(n));
