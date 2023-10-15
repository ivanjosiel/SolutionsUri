const readline = require('readline-sync');
const lines = readline.question('Informe o Raio: ');


const pi = 3.14159;
const r = parseFloat(lines);

const volume = (4/3.0) * pi * Math.pow(r, 3);

console.log('VOLUME = ' + volume.toFixed(3));
