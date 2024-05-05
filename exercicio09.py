from random import randint
vetor = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
indice = 0
soma = 0
numNegativos = 0

while indice < 10:
    vetor[indice] = randint(-100, 100)
    if vetor[indice] >= 1:
        soma += vetor[indice]
    else:
        numNegativos += 1
    indice += 1

print(f"a quantidade de números negativos é de {numNegativos}, e a soma é {soma}")
