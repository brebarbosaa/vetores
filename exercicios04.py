valores = [0, 0, 0, 0, 0, 0, 0, 0]
indice = 0

while indice < 8:
    numero = int(input("digite um número: "))
    valores[indice] = numero
    indice += 1


indice = int(input("escolha um valor x: "))
x = valores[indice]

indice = int(input("escolha um valor y: "))
y = valores[indice]

resultado = x + y
print("a soma desses valores é: ", resultado)
