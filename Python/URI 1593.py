n = int(input())

for i in range(n):

    entrada = int(input())
    binario = bin(entrada)
    b = list(binario)
    print(b.count("1"))
