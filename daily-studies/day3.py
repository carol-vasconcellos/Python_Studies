# tabuada de multiplicação
n = int(input("Digite um numero: "))

for i in range(1, 11):
    print(f'{i} x {n} = {i * n}')

# Soma dos 10 primeiros números

soma = 0 
for i in range(1, 11):
    soma += i

    print("A soma dos 10 primeiros números é:", soma)

# Contagem regressiva
n = int(input("Digite um número para a contagem regressiva: "))

while n > 0:
    print(n)
    n -= 1
print("Fogo!")