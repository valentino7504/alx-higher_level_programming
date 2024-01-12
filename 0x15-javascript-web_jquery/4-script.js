#!/usr/bin/node
// toggles a class
$('div#toggle_header').on('click', function () {
  $('header').toggleClass('green red');
});
