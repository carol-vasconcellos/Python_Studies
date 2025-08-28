import time

# Gerar lista de 1 milhão de números
lista = list(range(1, 1_000_001))
alvo = 1_000_000  # último número da lista

# --- Busca simples ---
inicio_simples = time.time()
for i, num in enumerate(lista):
    if num == alvo:
        passos_simples = i + 1  # contar passos
        break
fim_simples = time.time()
tempo_simples = fim_simples - inicio_simples

print(f"Busca simples encontrou {alvo} em {passos_simples} passos, tempo: {tempo_simples:.6f} s")

# --- Busca binária ---
def busca_binaria(lista, alvo):
    esquerda = 0
    direita = len(lista) - 1
    passos = 0
    while esquerda <= direita:
        passos += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return passos
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return passos

inicio_binaria = time.time()
passos_binaria = busca_binaria(lista, alvo)
fim_binaria = time.time()
tempo_binaria = fim_binaria - inicio_binaria

print(f"Busca binária encontrou {alvo} em {passos_binaria} passos, tempo: {tempo_binaria:.6f} s")
