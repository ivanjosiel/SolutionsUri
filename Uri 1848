gritos = 0
soma = 0
binario = []
while gritos<3:
    
    piscada = input()
    
    if piscada != 'caw caw':
        for i in piscada:
                if i == '-':
                    binario.append('0')
                if i == '*':
                    binario.append('1')
        binario = ''.join(binario)
    

        binario = int(binario, 2)
       
        soma += binario
        binario = []
    
    else:
        print(soma)
        soma = 0
        gritos += 1
        
