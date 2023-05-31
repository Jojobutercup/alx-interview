#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as a command-line argument');
  process.exit(1);
}

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Invalid request. Status Code:', response.statusCode);
  } else {
    const movie = JSON.parse(body);
    movie.characters.forEach((characterUrl) => {
      request(characterUrl, (err, res, charBody) => {
        if (err) {
          console.error('Error:', err);
        } else if (res.statusCode !== 200) {
          console.error('Invalid request. Status Code:', res.statusCode);
        } else {
          const character = JSON.parse(charBody);
          console.log(character.name);
        }
      });
    });
  }
});
