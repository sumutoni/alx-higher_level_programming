#!/usr/bin/node
exports.esrever = function (list) {
  const list1 = [];
  let i = list.length - 1;
  while (i >= 0) {
    list1.push(list[i]);
    i--;
  }
  return list1;
};
