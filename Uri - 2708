carros = 0
pessoas = 0
while True:
    entrada = list(map(str, input().split()))
    teste = entrada[0]
    if teste == "ABEND":
        break

    elif teste == "SALIDA":
        carros += 1
        val = entrada[1]
        pessoas += int(val)

    else:
        carros -= 1
        val = entrada[1]
        pessoas -= int(val)

print(pessoas)
print(carros)
