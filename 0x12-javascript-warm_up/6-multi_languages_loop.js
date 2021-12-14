#!/usr/bin/node

let i = 0;
let phrase = '';

for (; i < 3; i++) {
  switch (i) {
    case 0:
      phrase += 'C is fun\n';
      break;
    case 1:
      phrase += 'Python is cool\n';
      break;
    case 2:
      phrase += 'JavaScript is amazing';
      break;
  }
}

console.log(phrase);
