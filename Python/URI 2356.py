while True:
    try:
        
        d = input()
        s = input()
        
        proteinas = "AGCT"
        
        if s in d:
            print("Resistente")
        else:
            print("Nao resistente")
            
    except EOFError:
        break 
