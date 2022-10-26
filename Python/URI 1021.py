n = float(input())
print("NOTAS:")
cont = 0
resu = 0

while (n>=100):
    resu = n - 100
    cont += 1
    n = resu

print ("{} nota(s) de R$ 100.00".format(cont))
cont = 0

while (n>=50):
    resu = n - 50
    cont += 1
    n = resu

print ("{} nota(s) de R$ 50.00".format(cont))
cont = 0

while (n>=20):
    resu = n - 20
    cont += 1
    n = resu

print ("{} nota(s) de R$ 20.00".format(cont))
cont = 0

while (n>=10):
    resu = n - 10
    cont += 1
    n = resu

print ("{} nota(s) de R$ 10.00".format(cont))
cont = 0

while (n>=5):
    resu = n - 5
    cont += 1
    n = resu

print ("{} nota(s) de R$ 5.00".format(cont))
cont = 0

while (n>=2):
    resu = n - 2
    cont += 1
    n = resu

print ("{} nota(s) de R$ 2.00".format(cont))
cont = 0

#mededas
print("MOEDAS:")
while (n>=1):
    resu = n - 1
    cont += 1
    n = resu

print ("{} moeda(s) de R$ 1.00".format(cont))
cont = 0

nm = float("{0:.2f}".format(n))

while (nm>=0.50):
    resu = nm - 0.50
    cont += 1
    nm = resu
    nm = float("{0:.2f}".format(nm))
print ("{} moeda(s) de R$ 0.50".format(cont))
cont = 0

while (nm>=0.25):
    resu = nm - 0.25
    cont += 1
    nm = resu
    nm = float("{0:.2f}".format(nm))
print ("{} moeda(s) de R$ 0.25".format(cont))
cont = 0

while (nm>=0.10):
    resu = nm - 0.10
    cont += 1
    nm = resu
    nm = float("{0:.2f}".format(nm))
print ("{} moeda(s) de R$ 0.10".format(cont))
cont = 0

while (nm>=0.05):
    resu = nm - 0.05
    cont += 1
    nm = resu
    nm = float("{0:.2f}".format(nm))
print ("{} moeda(s) de R$ 0.05".format(cont))
cont = 0

while (nm>0.01) or (nm == 0.01):
    resu = nm - 0.01
    cont += 1
    nm = resu
    nm = float("{0:.2f}".format(nm))
print ("{} moeda(s) de R$ 0.01".format(cont))
