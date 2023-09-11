#!/usr/bin/node
const argv = process.argv;
function secondBiggest (values) {
  if (values.length === 2 || values.length === 3) {
    return (0);
  }
  values = values.slice(2);
  values.forEach((value, index) => {
    values[index] = Number(value);
  });
  let biggest = values[0];
  let prevBiggest = values[0];
  values.forEach(value => {
    if (value > biggest) {
      prevBiggest = biggest;
      biggest = value;
    }
  });
  return (prevBiggest);
}
console.log(secondBiggest(argv));
