#!/usr/bin/node
const fs = require('fs');
const file = process.argv[2];
const cont = process.argv[3];
fs.writeFile(file, cont, (err) => {
  if (err) {
    console.error(err);
  }
});
