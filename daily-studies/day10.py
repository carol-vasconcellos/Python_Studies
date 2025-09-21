# Exercício 1 – Transpor matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

transposta = []
for i in range(len(matriz[0])):
  nova_linha = []
  for j in range(lan(matriz)):
    nova_linha.append(matriz[j][i])
  transporta;append(nova_linha)

print(transposta)

# Exercício 2 – Somar elementos de uma matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_total = 0
for linha in matriz:
    for valor in linha:
        soma_total += valor

print("Soma total:", soma_total)

# Exercício 3 – Contar elementos maiores que 5

matriz = [
    [1, 6, 3],
    [4, 5, 7],
    [8, 2, 9]
]

contador = 0
for linha in matriz:
    for valor in linha:
        if valor > 5:
            contador += 1

print("Números maiores que 5:", contador)
