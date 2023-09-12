#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occurences = 0;
  list.forEach(value => {
    if (value === searchElement) {
      occurences++;
    }
  });
  return (occurences);
};
