# Função de busca simples
def busca_simples(lista, alvo):
    passos = 0
    for i in range(len(lista)):
        passos += 1
        if lista[i] == alvo:
            return i + 1, passos  # posição e passos
    return None, passos

# Função de busca binária que conta passos
def busca_binaria_com_passos(lista, alvo):
    passos = 0
    esquerda = 0
    direita = len(lista) - 1
    while esquerda <= direita:
        passos += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio + 1, passos  # posição e passos
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None, passos

# Testando as funções
numeros = list(range(1, 1001))
print(busca_simples(numeros, 999))  # último elemento
print(busca_simples(numeros, 1))    # primeiro elemento

indice, passos = busca_binaria_com_passos(numeros, 999)
print(f"Procurando {999} deve fazer {passos} passos")

indice, passos = busca_binaria_com_passos(numeros, 1)
print(f"Procurando {1} deve fazer {passos} passos")

# Tabela comparativa
print("Tamanho | Busca Simples | Busca Binária")
print("--------------------------------------")

for n in [10, 100, 1000, 10000]:
    numeros = list(range(1, n+1))
    alvo = n  # último elemento (pior caso para busca simples)
    _, passos_simples = busca_simples(numeros, alvo)
    _, passos_binaria = busca_binaria_com_passos(numeros, alvo)
    print(f"{n:7} | {passos_simples:13} | {passos_binaria:12}")
