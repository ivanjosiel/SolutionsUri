while True:
    try:
        tamanho_matriz = int(input())
        
        matriz = [[0 for i in range(tamanho_matriz)] for j in range(tamanho_matriz)] # definição do tamanho da matriz

        for i in range(tamanho_matriz):
            for j in range(tamanho_matriz):
                if i == j:
                    matriz[i][j] = 2
                elif i + j == tamanho_matriz-1:
                    matriz[i][j] = 3
                    
        submatriz_inicio = int(tamanho_matriz/3) # inicio do tamanho para adicionar o 1
        submatriz_final = int(tamanho_matriz-(submatriz_inicio))
        
        for i in range(submatriz_inicio, submatriz_final): #percorrendo  tamanho e adicionando 1 na matriz
            for j in range(submatriz_inicio, submatriz_final):
                matriz[i][j] = 1
        
        metade_matriz = int(tamanho_matriz/2)
        matriz[metade_matriz][metade_matriz] = 4

        for i in range(tamanho_matriz):
            for j in range(tamanho_matriz):
                if j != tamanho_matriz - 1:
                    print("{}".format(matriz[i][j]).rjust(0), end="")
                else:
                    print("{}".format(matriz[i][j]).rjust(0))
        print("")
    except EOFError:
        break
    
