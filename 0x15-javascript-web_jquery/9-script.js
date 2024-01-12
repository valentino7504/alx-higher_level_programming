#!/usr/bin/node
// fetches hello from a url
$(function () {
  $.ajax(
    {
      type: 'GET',
      dataType: 'json',
      url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
      success: function (data, status, xhr) {
        $('div#hello').text(data.hello);
      }
    }
  );
}
);
