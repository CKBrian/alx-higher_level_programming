#!/usr/bin/node
const request = require('request');
const Id = process.argv[2];
const url2 = `https://swapi-api.alx-tools.com/api/films/${Id}/`;

function printCharacter (url) {
  request(url, (err, resp, body) => {
    if (err) {
      console.log(err);
      return;
    }

    console.log(JSON.parse(body).name);
  });
}

request(url2, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }
  // character list
  const charList = JSON.parse(body).characters;
  charList.forEach(Url => printCharacter(Url));
});
