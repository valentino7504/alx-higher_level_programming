#!/usr/bin/node
// script that prints all the characters in a star wars
// movie
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  else {
    const filmDetails = JSON.parse(body);
    filmDetails.characters.forEach(characterURL => {
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
