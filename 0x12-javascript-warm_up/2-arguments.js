#!/usr/bin/node
/*
If no arguments are passed to the script, prints “No argument”
If only one argument is passed to the script, prints “Argument found”
Otherwise, prints “Arguments found”
 */
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
