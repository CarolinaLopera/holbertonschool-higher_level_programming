#!/usr/bin/node

const isNumber = parseInt(process.argv[2]);

if (isNaN(isNumber) === false) {
  console.log('My number:', isNumber);
} else {
  console.log('Not a number');
}
