#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;
for (let i = 2; i < 4; i++) {
  fs.readFile(argv[i], (err, file) => {
    if (err) throw err;
    fs.appendFile(argv[4], file.toString(), (err) => {
      if (err) throw err;
    });
  });
}
