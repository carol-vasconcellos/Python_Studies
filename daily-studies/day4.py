# criar uma lsita de numeros
lista = [10, 20, 30, 40]

soma = sum(lista)
print("A soma dos números da lista é:", soma)

dividir = soma / len(lista)
print("A média dos números da lista é:", dividir)

# encontrar o maior 
lista = [10, 20, 30, 40]

maior = max(lista)

for i in lista:
    if i == maior:
        maior = i
        print(f'O maior número da lista é: {maior}')

# Filtrar números pares

lista = [10, 15, 20, 25, 30, 35, 40]
pares = []

for i in lista:
    if i % 2 == 0:
        pares.append(i)
print("Números pares na lista:", pares)

