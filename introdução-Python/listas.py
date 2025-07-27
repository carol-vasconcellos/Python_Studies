numeros = []
for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

busca = int(input("Qual número deseja buscar? "))

if busca in numeros:
    print("Número encontrado!")
else:
    print("Número NÃO encontrado.")
