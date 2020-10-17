while True:
    try:
        ent = input()
        n_s = int(input())
        pos = [int(x) for x in input().split()]
        for i in pos:
            print(ent[i-1], end = '')
        print()
    except EOFError:
        break
