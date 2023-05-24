#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  const completed = {};
  if (!err) {
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (!completed[todo.userId.toString()]) {
        if (todo.completed) {
          completed[todo.userId.toString()] = 1;
        }
      } else {
        if (todo.completed) {
          completed[todo.userId.toString()] += 1;
        }
      }
    }
  }
  console.log(completed);
});
