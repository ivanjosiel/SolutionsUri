const readline = require('readline-sync');
const lines = readline.question();

var valores = lines.split(' ')

const pi = 3.14159

var a = parseFloat(valores[0])
var b = parseFloat(valores[1])
var c = parseFloat(valores[2])

var areaTriangulo = (a * c)/2
var areaCirculo = pi*(Math.pow(c, 2))
var areaTrapezio = ((a + b) * c)/2.0
var areaQuadrado = b * b
var areaRetangulo = a * b

console.log('TRIANGULO: ' + areaTriangulo.toFixed(3))
console.log('CIRCULO: ' + areaCirculo.toFixed(3))
console.log('TRAPEZIO: ' + areaTrapezio.toFixed(3))
console.log('QUADRADO: ' + areaQuadrado.toFixed(3))
console.log('RETANGULO: ' + areaRetangulo.toFixed(3))
