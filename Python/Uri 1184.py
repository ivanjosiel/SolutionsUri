operação = input()
soma = 0
cont_elementos = 0
diagonal = 0

for linha in range(12):
    for coluna in range(12):
        entrada = float(input())
        
        if coluna < diagonal:
            soma += entrada
            cont_elementos += 1 
    diagonal += 1 
if operação == 'S':
    print("{:.1f}".format(soma))
else:
    print("{:.1f}".format(soma/cont_elementos))
    
            
