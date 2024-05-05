valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numero = int(input("digite um número inteiro: "))
indice = 0
maior = numero
menor = numero

while indice < 9:
    numero = int(input("digite um número inteiro: "))
    valores[indice] = numero
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero
    indice += 1

print(f"o maior valor foi {maior} e o menor foi {menor}")
