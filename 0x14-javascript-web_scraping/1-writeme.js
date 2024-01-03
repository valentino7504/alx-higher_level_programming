#!/usr/bin/node
// writes astring to a file
const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];
fs.writeFile(filePath, fileContent, (error) => {
  if (error) {
    console.log(error);
  }
});
