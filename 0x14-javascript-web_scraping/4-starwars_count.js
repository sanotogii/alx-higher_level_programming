#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];
const charId = 18;

if (!apiUrl) {
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const films = JSON.parse(body).results;
    const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${charId}/`)).length;
    console.log(count);
  }
});
