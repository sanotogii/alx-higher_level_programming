#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const data = process.argv[3];

if (!filePath) {
  process.exit(1);
}

fs.writeFile(filePath, data, 'utf8', (err) => {
  if (err) {
    console.error(err);
  }
});
