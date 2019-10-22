while True:
    try:

        n = int(input())
        l = list(map(int, input().split()))

        maior = max(l)

        if maior<10:
            print(1)
        elif maior>=10 and maior<20:
            print(2)
        elif maior>=20:
            print (3)

    except EOFError:
        break
