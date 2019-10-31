num = float(input())

if num >= 0 and num <= 25:
    print('Intervalo [0,25]'.format(num))
elif num > 25 and num <= 50:
    print('Intervalo (25,50]')
elif num > 50 and num <= 75:
    print('Intervalo (50,75]'.format(num))
elif num > 75 and num <= 100:
    print('Intervalo (75,100]'.format(num))
else:
    print('Fora de intervalo')
