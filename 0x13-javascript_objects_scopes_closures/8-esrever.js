#!/usr/bin/node

exports.esrever = function (list) {
  const lis = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    lis[j] = list[i];
    j++;
  }
  return lis;
};
