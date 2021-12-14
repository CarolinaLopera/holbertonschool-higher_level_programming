#!/usr/bin/node

const number = parseInt(process.argv[2]);
let x = '';
let i, j;

if (isNaN(number) === false) {
  for (i = 0; i < number; i++) {
    for (j = 1; j < number; j++) {
      x += 'X';
    }
    x += 'X';
    if (i < number - 1) {
      x += '\n';
    }
  }
  if (number > 0) {
    console.log(x);
  }
} else {
  console.log('Missing size');
}
