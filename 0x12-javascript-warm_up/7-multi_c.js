#!/usr/bin/node
/*
 prints x times “C is fun”
Where x is the first argument of the script
If the first argument can’t be converted to an integer, it prints “Missing number of occurrences”
 */
const num = Number(process.argv[2]);
let i = 0;

if (typeof (num) === 'number' && !isNaN(num)) {
  while (i < num) {
    console.log('C is fun');
    i++;
  }
} else {
  console.log('Missing number of occurrences');
}
