notas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
indice = 0
soma = 0

while indice < 15:
    nota = int(input("digite a nota do aluno: "))
    notas[indice] = nota
    soma+=nota
    indice += 1
resultado = soma/15

print(f"a média dos alunos foi de {resultado}")
