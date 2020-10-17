import math
numero = int(input())

log = math.log(numero)
minimo = numero/log
maximo = 1.25506*(numero/log)

print("{:.1f} {:.1f}".format(minimo, maximo))
