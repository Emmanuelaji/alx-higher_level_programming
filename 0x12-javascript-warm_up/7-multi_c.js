#!/usr/bin/node
const occurence = parseInt(process.argv[2], 10);
const text = 'C is fun';

if (occurence) {
  for (let i = 0; i < occurence; i++) {
    console.log(text);
  }
} else {
  console.log('Missing number of occurrences');
}
