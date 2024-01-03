#!/usr/bin/node
// gets the number of starwars movies Wedge Antilles is in
const request = require('request');
const characterID = 18;
const charactersURL = 'https://swapi-api.alx-tools.com/api/people/';
const url = process.argv[2];
request(url, (error, response, body) => {
  let wedgeMovies = 0;
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    movies.forEach(movie => {
      if (movie.characters.includes(charactersURL + characterID + '/')) {
        wedgeMovies++;
      }
    });
  }
  console.log(wedgeMovies);
});
