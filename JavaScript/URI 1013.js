var input = require('fs').readFileSync('/dev/stdin', 'utf8');
var lines = input.split('\n');

var valores = lines.shift().split(' ')

var a = parseFloat(valores[0])
var b = parseFloat(valores[1])
var c = parseFloat(valores[2])

var maiorAB = (a + b + Math.abs(a-b))/2

if (maiorAB > c){
  console.log(maiorAB + ' eh o maior')
} else{
  console.log(c + ' eh o maior')
}
