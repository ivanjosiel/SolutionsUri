while True:
    try:
        n = int(input())
        
        velocidade = list(map(int, input().split()))
        
        maior = max(velocidade)
        
        if maior<10:
            print("1")
        elif maior <20:
            print("2")
        else:
            print("3")
    except EOFError:
        break
        
