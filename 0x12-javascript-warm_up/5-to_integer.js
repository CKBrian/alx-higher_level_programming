#!/usr/bin/node
/*
 prints My number: <first argument converted in integer> if the first argument can be converted to an integer:

If the argument can’t be converted to an integer, print “Not a number”
 */
const argv1 = process.argv[2];
if (typeof (Number(argv1)) === 'number') {
  console.log(`My number: ${argv1}`);
} else {
  console.log('Not a number');
}
