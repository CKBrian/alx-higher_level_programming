#!/usr/bin/node

const fs = require('fs');
const filename = process.argv[2];
console.log(filename);
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
