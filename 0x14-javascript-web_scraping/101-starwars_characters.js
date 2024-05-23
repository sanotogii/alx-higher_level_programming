#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

if (!movieId) {
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;
    const characterNames = [];

    function printCharacterNames (index) {
      if (index >= characters.length) {
        characterNames.forEach(name => console.log(name));
        return;
      }

      request(characters[index], (charError, charResponse, charBody) => {
        if (charError) {
          console.error(charError);
        } else {
          const character = JSON.parse(charBody);
          characterNames.push(character.name);
          printCharacterNames(index + 1);
        }
      });
    }

    printCharacterNames(0);
  }
});
