while True:
    a, b = map(int,input().split())

    if a == 0 and b == 0:
        break
    else:
        resultado = 2*a - b
        print(resultado)
