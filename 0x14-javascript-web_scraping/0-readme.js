#!/usr/bin/node

let fs = require('fs');
fs.readFile(process.argv[2], 'utf8', bar);

function bar(err, data) {
    err ? console.log(err): console.log(data);
};
