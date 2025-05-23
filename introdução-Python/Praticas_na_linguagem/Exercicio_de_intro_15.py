'''Crie um programa que peça um número `n` e:

1. Mostre todos os pares de `1` até `n`. (`O(n)`)
2. Mostre todos os pares de combinações possíveis de `1` até `n`. (`O(n²)`)'''

n = int(input("Digite um número: "))

print("\nNúmeros pares de 1 até n (O(n)):")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\n\nTodas as combinações de 1 até n (O(n²)):")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"({i}, {j})", end=" ")