#!/usr/bin/node
/*
 prints the first argument passed to it:

If no arguments are passed to the script, prints “No argument”
You must use console.log(...) to prints all output
 */
if (!process.argv[2]) {
  console.log('No argument');
} else {
  console.log(`${process.argv[2]}`);
}
