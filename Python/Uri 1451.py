while True:
    try:
        texto_entrada = input()
        
        inicio = ""
        meio = ""
        fim = ""
        
        flag_abertura = 0
        flag_normal = 1
        flag_fechamento = 2
        flag_atual = flag_normal
        
        for letra in texto_entrada:
            
            if letra == "[": # verificação do estado inicial da flag atual (alteração)
                flag_atual = flag_abertura
                meio = inicio + meio
                inicio = ""
                continue
            elif letra == "]":
                flag_atual = flag_fechamento
                meio = meio + fim 
                fim = ""
                continue
            
            if flag_atual == flag_normal: # verificação de estado da letra
                meio += letra
            elif flag_atual == flag_fechamento:
                fim += letra
            else:
                inicio += letra
            
        print(inicio+meio+fim)
            
    except EOFError:
        break
                
                
