#!/usr/bin/node
const url = process.argv[2];
const request = require('request');

function userList (ls, id) {
  const newList = ls.filter((item) => item.userId === id && item.completed);
  return newList.length;
}

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  }

  const list = JSON.parse(body);
  for (let i = 1; i < 11; i++) {
    const uId = i;
    if (i === 1) {
      console.log(`{\n  '${uId}': ${userList(list, uId)},`);
    } else if (i === 10) {
      console.log(`  '${uId}': ${userList(list, uId)}\n}`);
    } else {
      console.log(`  '${uId}': ${userList(list, uId)},`);
    }
  }
});
