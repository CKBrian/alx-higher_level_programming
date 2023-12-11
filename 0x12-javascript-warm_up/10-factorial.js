#!/usr/bin/node
/*
 computes and prints a factorial

The first argument is integer (argument can be cast as integer) used for computing the factorial
Factorial of NaN is 1
 */
function factorial (num) {
  if (num === 1 || isNaN(num)) return 1;
  return factorial(num - 1) * num;
}

const num1 = parseInt(process.argv[2]);
console.log(`${factorial(num1)}`);
