import random

# -------------------------------
# Exercício 1 – Menor elemento
# -------------------------------
def indice_menor(lista):
    """
    Deve retornar o índice do menor elemento da lista.
    Exemplo: [5, 3, 6, 2, 10] → retorna 3
    """
    menor = lista[0]
    idx_menor = 0
    
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            idx_menor = i
    return idx_menor

print(indice_menor([5, 3, 6, 2, 10]))   # Deve retornar 3


# -------------------------------
# Exercício 2 – Ordenação por seleção
# -------------------------------
def ordena_por_selecao(lista):
    """
    Usando indice_menor, cria uma nova lista ordenada.
    Exemplo: [5, 3, 6, 2, 10] → [2, 3, 5, 6, 10]
    """
    ordenada = []
    copia = lista[:]
    
    while len(copia) > 0:
        idx = indice_menor(copia)
        menor = copia.pop(idx)
        ordenada.append(menor)
    
    return ordenada

print(ordena_por_selecao([5, 3, 6, 2, 10]))  # Deve retornar [2, 3, 5, 6, 10]


# -------------------------------
# Exercício 3 – Contador de passos
# -------------------------------
def indice_menor_com_passos(lista):
    """
    Retorna o índice do menor elemento e o número de comparações feitas.
    """
    menor = lista[0]
    idx_menor = 0
    comparacoes = 0
    
    for i in range(1, len(lista)):
        comparacoes += 1
        if lista[i] < menor:
            menor = lista[i]
            idx_menor = i
    return idx_menor, comparacoes

# Testando a função indice_menor_com_passos
lista_teste = [5, 3, 6, 2, 10]
idx, comp = indice_menor_com_passos(lista_teste)
print("Índice do menor elemento:", idx)   # Deve ser 3
print("Número de comparações feitas:", comp)  # Deve ser 4



def ordena_por_selecao_com_passos(lista):
    """
    Ordena a lista usando seleção, contando comparações.
    Retorna (lista_ordenada, total_comparacoes).
    """
    ordenada = []
    copia = lista[:]
    total_comparacoes = 0

    while len(copia) > 0:
        idx, comp = indice_menor_com_passos(copia)
        total_comparacoes += comp
        menor = copia.pop(idx)
        ordenada.append(menor)

    return ordenada, total_comparacoes

print(ordena_por_selecao_com_passos([5, 3, 6, 2, 10]))


# -------------------------------
# Exercício 4 – Comparação com sort()
# -------------------------------
def compara_com_sort():
    """
    Gera uma lista de 100 números aleatórios e compara ordenação.
    """
    lista = [random.randint(0, 1000) for _ in range(100)]
    
    # Ordenação por seleção contando comparações
    ordenada, passos = ordena_por_selecao_com_passos(lista)
    print("Número de comparações na seleção:", passos)
    
    # Ordenação com sort do Python
    lista_sort = lista[:]
    lista_sort.sort()
    
    # Verificação se são iguais
    print("As duas listas são iguais?", ordenada == lista_sort)

compara_com_sort()
