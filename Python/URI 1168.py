leds = {
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6,
    "0": 6,
    }

casos_Teste = int(input())

for i in range(casos_Teste):
    entrada =input()
    count = 0
    
    for num in entrada:
       count += leds[num]
    print(count, 'leds')
        

    



    
