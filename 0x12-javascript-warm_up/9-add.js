#!/usr/bin/node
/*
 prints the addition of 2 integers

The first argument is the first integer
The second argument is the second integer
You have to define a function with this prototype: function add(a, b)
 */
function add (a, b) {
  return a + b;
}
const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);
if (!isNaN(num1) || !isNaN(num2)) {
  console.log(`${add(num1, num2)}`);
}
