while True:
    try:
        n = int(input())

        for i in range(1,n+1, 2):
            valor = "*"*i
            print(valor.center(n).rstrip())

        for i in range (1,4,2):
            caule = "*"*i
            print(caule.center(n).rstrip())
        print()

    except EOFError:
        break
