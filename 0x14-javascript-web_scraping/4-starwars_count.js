#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url, function (err, response, body) {
  let count = 0;
  if (!err) {
    const films = JSON.parse(body).results;
    for (const film of films) {
      const characters = film.characters;
      for (const character of characters) {
        if (/18/.test(character)) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
