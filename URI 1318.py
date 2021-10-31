while(True):
    n,m = list(map(int,input().split()))
    if(n==m==0):
        break
    c = list(input().split())
    cont = 0
    d = list(set(c))
    for z in range(len(d)):
        if(c.count(d[z])>1):
            cont+=1
    print(cont)