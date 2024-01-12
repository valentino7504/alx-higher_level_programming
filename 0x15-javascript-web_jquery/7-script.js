#!/usr/bin/node
// fetches character name from url
$.ajax(
  {
    type: 'GET',
    dataType: 'json',
    url: 'https://swapi.dev/api/people/5/?format=json',
    success: function (data, status, xhr) {
      $('div#character').text(data.name);
    }
  }
);
