# -*- coding: utf-8 -*-

n = int(input())
km = 0

for i in range(n):
    x, y = map(int, input().split())
    km += x * y

print(km)