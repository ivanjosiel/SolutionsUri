import math
v, n = map(int, input().split())
for i in range(10, 100, 10):
	valor = ((v*n)*(i/100))
	if i == 90:
		print(math.ceil(valor))

	else:
		print(math.ceil(valor), end = " ")
