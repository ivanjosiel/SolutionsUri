teste = int(input())
lista_chicotadas = list(map(int,input().split()))
menor = min(lista_chicotadas)
print(lista_chicotadas.index(menor)+1)
    
