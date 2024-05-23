#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];

if (!url || !filePath) {
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('code:', response.statusCode);
    return;
  }

  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
