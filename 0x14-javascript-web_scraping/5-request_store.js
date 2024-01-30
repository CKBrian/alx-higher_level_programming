#!/usr/bin/node
const filename = process.argv[3];
const url = process.argv[2];
const fs = require('fs');
const request = require('request');

request(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  }
  fs.writeFile(filename, body, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
