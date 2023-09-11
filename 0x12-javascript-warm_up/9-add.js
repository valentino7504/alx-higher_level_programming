#!/usr/bin/node
function add (a, b) {
  a = Number(a);
  b = Number(b);
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  }
  return (a + b);
}
const argv = process.argv;
console.log(add(argv[2], argv[3]));
