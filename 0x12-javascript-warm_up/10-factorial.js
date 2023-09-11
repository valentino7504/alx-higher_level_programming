#!/usr/bin/node
function factorial (value) {
  if (isNaN(value) || value === 1 || value === 0) {
    return (1);
  }
  return (value * factorial(value - 1));
}
const argv = process.argv;
console.log(factorial(Number(argv[2])));
