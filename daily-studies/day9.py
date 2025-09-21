# Exercício 1 – Tabuada com loop duplo

for i in range(1,6):
  for j in range(1, 6):
    print(f"{i} x {j} = {i * j}")
  print("-" * 10)

# Exercício 2 – Somar elementos de uma matriz

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma = 0 
for linha in matriz:
  for valor in linha:
    soma += valor

print("Soma total:", soma)

# Exercício 3 – Desenhar um quadrado de #

n = 4
for i in range(n):
  for j in range(n):
    print("#", end=" ")
  print

