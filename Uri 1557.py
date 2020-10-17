while True:
    matriz = []
    tamanho_matriz = int(input())
    
    if tamanho_matriz == 0:
        break
    
    for i in range(0,tamanho_matriz):
        linha = []
        j = i
        for j in range(i, tamanho_matriz+i):
            valor = 2 ** j
            linha.append(valor)
        matriz.append(linha)
    
    digitos = len(str(matriz[-1][-1]))
   
    for i in range(tamanho_matriz):
        for j in range(tamanho_matriz):
            if j != tamanho_matriz - 1:
                 print("{}".format(matriz[i][j]).rjust(digitos), end=" ")
            else:
                print("{}".format(matriz[i][j]).rjust(digitos))
    print("")
    
            
