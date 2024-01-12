#!/usr/bin/node
// fetches and lists all movies
$.ajax(
  {
    type: 'GET',
    dataType: 'json',
    url: 'https://swapi.dev/api/films/?format=json',
    success: function (data, status, xhr) {
      data.results.forEach(movie => {
        $('ul#list_movies').append(
          '<li>' +
          movie.title +
          '</li>'
        );
      });
    }
  }
);
