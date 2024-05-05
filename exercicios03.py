valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
resultado = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
indice = 0

while indice < 10:
    numero = int(input("digite um número: "))
    valores[indice] = numero
    indice += 1
indice = 0
while indice < 10:
    resultado[indice] = valores[indice] ** 2
    indice += 1
print("os valores desse vetor ao quadrado é: ", resultado)
