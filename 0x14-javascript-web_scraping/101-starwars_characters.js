#!/usr/bin/node
// script that prints all the characters in a star wars
// movie
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const movieId = process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const films = JSON.parse(body).results;
    let film;
    for (let i = 0; i < films.length; i++) {
      if (films[i].episode_id.toString() === movieId) {
        film = films[i];
        break;
      }
    }
    film.characters.forEach(characterURL => {
      request(characterURL, (error, response, body) => {
        if (error) console.log(error);
        else {
          const charDetails = JSON.parse(body);
          console.log(charDetails.name);
        }
      });
    });
  }
});
