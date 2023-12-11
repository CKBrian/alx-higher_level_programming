#!/usr/bin/node
/*
prints a square

The first argument is the size of the square
print “Missing size” if the first argument can’t be converted to an integer
 */
const sideLength = parseInt(process.argv[2]);

if (!isNaN(sideLength)) {
  for (let i = 0; i < sideLength; i++) {
    console.log('X'.repeat(sideLength));
  }
} else {
  console.log('Missing size');
}
