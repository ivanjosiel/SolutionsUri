p, q = map(int, input().split())

if p == 1:
    total = q*4.00
    print('Total: R$ {:.2f}'.format(total))
elif p == 2:
    total = q*4.50
    print('Total: R$ {:.2f}'.format(total))
elif p == 3:
    total = q*5.00
    print('Total: R$ {:.2f}'.format(total))
elif p == 4:
    total = q*2.00
    print('Total: R$ {:.2f}'.format(total))
elif p == 5:
    total = q*1.5
    print('Total: R$ {:.2f}'.format(total))
