#!/usr/bin/node

const request = require('request');
const Id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

if (!Id) {
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.log(error.code);
  }

  if (response.statusCode !== 200) {
    console.log('code:', response.statusCode);
  } else {
    const json = JSON.parse(body);
    console.log(json.title);
  }
}
);
