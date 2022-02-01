#!/usr/bin/node

const request = require('https');

request.get(process.argv[2], res => {
  console.log('code: ', res.statusCode);
});
