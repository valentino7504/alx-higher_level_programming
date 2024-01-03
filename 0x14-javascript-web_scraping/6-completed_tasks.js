#!/usr/bin/node
// gets ompleted tasks from the json placeholder api
const request = require('request');
const url = process.argv[2];
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const tasks = JSON.parse(body);
    const tasksObj = {};
    tasks.forEach(task => {
      const id = task.userId;
      if (task.completed) {
        if (Object.prototype.hasOwnProperty.call(tasksObj, id)) {
          tasksObj[id]++;
        } else {
          tasksObj[id] = 1;
        }
      }
    });
    console.log(tasksObj);
  }
});
