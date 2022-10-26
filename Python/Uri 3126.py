c = int(input())
parti = list(map(int,input().split()))
cont = 0

for i in range (len(parti)):
    if parti[i] == 1:
        cont += 1 
print(cont)

