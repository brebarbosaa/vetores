valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
indice = 0
numPares = 0
numImpares = 0


while indice < 10:
    numero = int(input("digite um número: "))
    valores[indice] = numero
    if valores[indice] % 2 == 0:
        numPares += 1
    else:
        numImpares += 1
    indice += 1

print("a quantidade de números pares é de: ", numPares)
