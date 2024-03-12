#!/usr/bin/node
const fs = require('fs');

const data1 = fs.readFileSync(process.argv[2]).toString();
const data2 = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], data1 + data2);