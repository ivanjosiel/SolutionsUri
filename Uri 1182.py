coluna = int(input())
operacao = input()

cont = 0
soma = 0

for i in range(12):
    for j in range(12):
        entrada = float(input())
        
        if j == coluna:
            soma += entrada
            cont+=1
if operacao == "S":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/cont))
    
    
