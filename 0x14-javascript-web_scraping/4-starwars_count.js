#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (err, resp, body) => {
  if (err) {
    console.log(err);
    return;
  }

  const films = JSON.parse(body).results;
  const list = films.filter(film =>
    film.characters.some(character => character.endsWith('/18/'))
  );
  console.log(list.length);
});
