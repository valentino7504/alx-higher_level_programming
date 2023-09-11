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
  const biggest = Math.max(...values);
  const newArray = values.filter(function (x) {
    return (x !== biggest);
  });
  return (Math.max(...newArray));
}
console.log(secondBiggest(argv));
