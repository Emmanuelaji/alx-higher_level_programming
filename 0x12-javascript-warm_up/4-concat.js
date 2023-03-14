#!/usr/bin/node
/*
 * save 1st arg to const var
 * save 2nd arg to const var
 * use formatted string in to log to console
 */
const firstArg = process.argv[2];
const secondArg = process.argv[3];

console.log(`${firstArg} is ${secondArg}`);
