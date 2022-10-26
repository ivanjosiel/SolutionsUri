n = int(input())
uni = list(map(int,input().split()))

soma = 0
for i in range (len(uni)):
    div = (uni[i]//3)*3
    soma += div 
print(soma)
        
        
