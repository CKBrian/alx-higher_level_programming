#!/usr/bin/node
/* imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence. */
const fs = require('fs');
const strArr = [];
fileA = process.argv[2];
fileB = process.argv[3];
fileC = process.argv[4];
fs.readFile('fileA', 'utf8', (err, data) => {
  if (!err) {
    strArr[0] = data;
  }
}
);
fs.readFile('fileB', 'utf8', (err, data) => {
  if (!err) {
    strArr[1] = data;
  }
}
);
const res = strArr.join('\n');
fs.writeFile(fileC, res);
