valores = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numero = int(input("digite um número inteiro: "))
indice = 0
maior = numero
maiorIndice = 0

while indice < 9:
    numero = int(input("digite um número inteiro: "))
    if numero > maior:
        maior = numero
        maiorIndice = indice
    valores[indice] = numero
    indice += 1

print(f"o maior valor digitado foi {maior} e a posição é {maiorIndice}")
