n = int(input())

for i in range(n):

    frase = input()

    fraseSemEspaco = ""  # variavel intermediaria que ira receber os caracteres da frase

    for letra in frase:
        if letra.isalpha():  # verificando se o caracter e alpabetico
            fraseSemEspaco += letra

    semLetrasRepetidas = set(fraseSemEspaco)  # retirando letras repetidas
    tamanho = len(semLetrasRepetidas)  # pegando a quantidade de letras

    if tamanho < 13:
        print("frase mal elaborada")

    elif (tamanho >= 13) and (tamanho < 26):
        print("frase quase completa")

    else:
        print("frase completa")
