'''

Funções que recebem listas

def maior_valor(lista):
    return max(lista)


Funções que aplicam filtro

def filtrar_pares(lista):
    return [n for n in lista if n % 2 == 0]


Funções com múltiplas condições

def classificar_numero(n):
    if n > 0:
        return "positivo"
    elif n < 0:
        return "negativo"
    else:
        return "zero"

'''

# Exercício 1 – Média apenas dos números positivos

def media_positivos(lista):
    positivos = [n for n in lista if n > 0]
    if not positivos:
        return 0
    return sum(positivos) / len(positivos)

print(media_positivos([-10, -5, 0, 5, 10]))  # Saída: 7.5

# Exercício 2 – Contar quantos números pares e ímpares existem

def contar_pares_impares(lista):
    pares = 0
    impares = 0
    for n in lista:
        if n % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

print(contar_pares_impares([1, 2, 3, 4, 5, 6]))

# Exercício 3 – Substituir números negativos por zero

def substituir_negativos(lista):
    nova_lista = []
    for n in lista:
        if n < 0:
            nova_lista.append(0)
        else:
            nova_lista.append(n)
    return nova_lista

print(substituir_negativos([-3, 5, -1, 7]))