# Soma dos N primeiros números

n = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, n + 1):
    soma += i

print("A soma de 1 até", n, "é:", soma)

# Média de N números

quantidade = int(input("Quantos números você vai digitar? "))
soma = 0

for i in range(quantidade):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / quantidade
print("A média dos números é:", media)

# Contagem regressiva personalizada

inicio = int(input("Digite o número inicial: "))
fim = int(input("Digite o número final: "))

passo = 1 if inicio < fim else -1

for i in range(inicio, fim + passo, passo):
    print(i)
