#!/usr/bin/node
// prints the title of a star wars movie depending on the
// id given
const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieID;
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movieDetails = JSON.parse(body);
    console.log(movieDetails.title);
  }
});
