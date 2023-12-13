#!/usr/bin/node
/* imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence. */
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];
fs.readFile(fileA, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }

  fs.writeFile(fileC, data, (err) => {
    if (err) {
      console.log(err);
    }
  }
  );
}
);
fs.readFile(fileB, 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  }

  fs.writeFile(fileC, data, { encoding: 'utf8', flag: 'a' }, (err) => {
    if (err) {
      console.log(err);
    }
  });
}
);
