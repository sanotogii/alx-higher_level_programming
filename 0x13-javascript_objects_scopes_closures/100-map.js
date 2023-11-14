#!/usr/bin/node
const initialList = require('./100-data');
console.log(initialList);
console.log(initialList.map((value, index) => value * index));
