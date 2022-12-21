#!/usr/bin/node
const args = parseInt(process.argv[2]);

if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < args; i++) {
    let drawer = '';
    for (let j = 0; j < args; j++) {
      drawer += 'X';
    }
    console.log(drawer);
  }
}
