permutacao = input()
frase_criptografada = input()


alphabeto = 'abcdefghijklmnopqrstuvwxyz'
index = []
saida = ''

for i in frase_criptografada:
    index.append(alphabeto.find(i))

for i in index:
    saida += permutacao[i]
print(saida)
