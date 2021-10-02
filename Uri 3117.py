n, k = map(int, input().split())

alunos = list(map(int, input().split()))
cont = 0
for i in range (len(alunos)):
    if alunos[i]<=0:
        cont+= 1 
if cont >= k:
    print("YES")
else:
    print("NO")
