import math

while True:
    n = int(input())

    if (n == 0): break

    rita, uilton, ingred = 0, 0, 0
#   3       2       2
    for j in range(n):
        u, r, i = map(int, input().split())

        if ((math.log(u) / math.log(2)) % 2 == 0 or u == 2):
            uilton += 1
            if u > r and u > i:
                uilton += 1
        if ((math.log(r) / math.log(2)) % 2 == 0 or r == 2):
            rita += 1
            if r > u and r > i:
                rita += 1
        if ((math.log(i) / math.log(2)) % 2 == 0 or i == 2):
            ingred += 1
            if i > r and i > u:
                ingred += 1

    if uilton > rita and uilton > ingred: res = "Uilton"
    elif rita > uilton and rita > ingred: res = "Rita"
    elif ingred > rita and ingred > uilton: res = "Ingred"
    else: res = "URI"

    print(res)
