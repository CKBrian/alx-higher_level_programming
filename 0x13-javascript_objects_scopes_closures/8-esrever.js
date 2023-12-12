#!/usr/bin/node
// returns the reversed version of a list
exports.esrever = function (list) {
  const newArr = [];
  let arrSize = list.length - 1;
  for (let j = 0; j < list.length; j++) {
    newArr[j] = list[arrSize--];
  }
  return newArr;
};
