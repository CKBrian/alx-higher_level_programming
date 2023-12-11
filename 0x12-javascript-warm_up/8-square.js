#!/usr/bin/node
/*
prints a square

The first argument is the size of the square
print “Missing size” if the first argument can’t be converted to an integer
 */
const sideLength = Number(process.argv[2]);

if (sideLength > 0 && typeof (sideLength) === 'number' && !isNaN(sideLength)) {
  for (let i = 0; i < sideLength; i++) {
    console.log('x'.repeat(sideLength));
  }
} else {
  console.log('Missing size');
}
