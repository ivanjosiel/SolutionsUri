n = int(input())
while n != 0:
    num = 0
    a = 0
    lista = list(map(int, input().split()))
    ord = sorted(lista)
    a = ord[-2]

    for i in range(len(lista)):
        if lista[i] == a:
            print(i+1)

    n = int(input())
