#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;
const targetUrl = 'https://swapi-api.alx-tools.com/api/people/18/';

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const films = JSON.parse(body);
  const characters = films.results;

  for (let i = 0; i < characters.length; i++) {
    const urlList = characters[i].characters;

    for (let j = 0; j < urlList.length; j++) {
      if (targetUrl === urlList[j]) {
        counter = counter + 1;
        break;
      }
    }
  }
  console.log(counter);
});
