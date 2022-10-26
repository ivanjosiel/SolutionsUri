n = int(input())
for i in range(n):
    entrada = input()

    if entrada[0] == entrada[2]:
        mult = int(entrada[0]) * int(entrada[2])
        print(mult)

    elif entrada[1].isupper():
        soma = int(entrada[2]) - int(entrada[0])
        print(soma)

    elif entrada[1].islower():
        sub = int(entrada[0]) + int(entrada[2])
        print(sub)
