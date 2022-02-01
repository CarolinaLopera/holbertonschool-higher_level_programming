#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], res => {
  console.log('code: ', res.statusCode);
});
