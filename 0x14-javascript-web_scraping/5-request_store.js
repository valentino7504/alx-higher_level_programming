#!/usr/bin/node
// gets content of a webpage and stores it in a file
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filePath = process.argv[3];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = body;
    fs.writeFile(filePath, content, (error) => {
      if (error) console.log(error);
    });
  }
});
