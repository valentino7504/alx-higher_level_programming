#!/usr/bin/node
const argv = process.argv;
let i = 0;
while (argv[i]) {
  if (i === 2) {
    console.log(argv[i]);
  }
  i++;
}
if (i === 2) {
  console.log('No argument');
}
