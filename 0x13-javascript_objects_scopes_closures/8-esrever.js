#!/usr/bin/node
exports.esrever = function (list) {
  const lastIndex = list.length - 1;
  for (let i = 0; i < (list.length) / 2; i++) {
    const temp = list[i];
    list[i] = list[lastIndex - i];
    list[lastIndex - i] = temp;
  }
  return (list);
};
