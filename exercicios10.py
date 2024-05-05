vetor = [0, 0, 0, 0, 0]
numero = int(input("digite um número: "))
indice = 1
soma = numero
maior = numero
menor = numero

while indice < 5:
    numero = int(input("digite um número: "))
    vetor[indice] = numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    soma += numero
    indice += 1

print(f"o vetor lido foi {vetor}, o maior número foi {maior}, o menor foi {menor} e a média é {soma/5}")
