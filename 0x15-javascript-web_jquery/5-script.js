#!/usr/bin/node
// adds a li item
$('div#add_item').on('click', function () {
  $('ul.my_list').append('<li>Item</li>');
});
