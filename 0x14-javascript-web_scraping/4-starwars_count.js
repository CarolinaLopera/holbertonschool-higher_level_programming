#!/usr/bin/node

const request = require('request');
let count = 0;

request(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body).results;
    for (const key of data) {
      for (const characters of key.characters) {
        if (characters.includes('18')) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
