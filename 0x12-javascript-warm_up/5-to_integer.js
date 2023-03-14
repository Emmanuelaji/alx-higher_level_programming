#!/usr/bin/node
const firstArg = process.argv[2];
const argToInt = parseInt(firstArg);

if (argToInt) {
  console.log(`My number: ${argToInt}`);
} else {
  console.log('Not a number');
}
