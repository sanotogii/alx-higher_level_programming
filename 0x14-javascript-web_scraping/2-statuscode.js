#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

if (!url) {
    process.exit(1);
}

request(url, (error, response) => {
  if (error) {
    console.log(error.code);
    process.exit(1);
  } else {
    console.log('code:', response.statusCode);
  }
});
