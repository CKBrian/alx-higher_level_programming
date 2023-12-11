#!/usr/bin/node
/*
searches the second biggest integer in the list of arguments.

all arguments can be converted to integer
prints 0 if no argument passed
prints 0 if the number of arguments is 1
 */
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  const sortedList = process.argv.slice(2).sort();
  const item = sortedList.length - 2;
  console.log(sortedList[item]);
}
