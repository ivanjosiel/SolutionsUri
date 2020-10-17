operacao = input()

soma = 0
cont_elementos = 0
diagonal_maior = 11
diagonal_menor = 0

for linha in range(12):
    for coluna in range(12):
        entrada = float(input())
        
        if coluna > diagonal_menor and coluna < diagonal_maior:
            soma += entrada
            cont_elementos += 1 
    diagonal_maior -= 1
    diagonal_menor += 1 
    
if operacao == "S":
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/cont_elementos))
