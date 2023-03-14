#!/usr/bin/node

/*
 * access the arguments
 * convert args to nums
 * sort nums
 * print second biggest num using its index
 */

const args = process.argv;
const num = args.slice(2, process.argv.length).sort((a, b) => a - b);

if (args.length <= 3) {
  console.log(0);
} else {
  console.log(num[num.length - 2]);
}
