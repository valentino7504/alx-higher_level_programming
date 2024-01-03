#!/usr/bin/node
// gets the number of starwars movies Wedge Antilles is in
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  let wedgeMovies = 0;
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).results;
    movies.forEach(movie => {
      if (movie.characters.some(person => person.includes('18'))) {
        wedgeMovies++;
      }
    });
  }
  console.log(wedgeMovies);
});
