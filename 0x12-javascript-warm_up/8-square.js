#!/usr/bin/node

const number = parseInt(process.argv[2]);
let x = '';
let i, j;

if (isNaN(number) === false) {
  for (i = 0; i < number; i++) {
    for (j = 1; j < number; j++) {
      x += 'x';
    }
    x += 'x';
    if (i < number - 1) {
      x += '\n';
    }
  }
  console.log(x);
} else {
  console.log('Missing size');
}
