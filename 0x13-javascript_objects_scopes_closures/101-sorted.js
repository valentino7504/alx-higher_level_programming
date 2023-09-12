#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
Object.entries(dict).forEach(entry => {
  if (entry[1] in newDict) {
    newDict[entry[1]].push(entry[0]);
  } else {
    newDict[entry[1]] = [entry[0]];
  }
});
console.log(newDict);
