#!/usr/bin/node
/*
 increments and calls a function.

The function must be visible from outside
Prototype: function (number, theFunction)
 */
module.exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
