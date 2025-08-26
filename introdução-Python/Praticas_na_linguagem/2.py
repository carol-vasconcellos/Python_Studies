numeros = [2, 4, 6, 8, 10, 12, 14, 16]

def busca_binaria(lista, alvo):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == alvo:
            return meio
        if chute > alvo:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

print(busca_binaria(numeros, 10))  # Saída: 4
print(busca_binaria(numeros, 3))   # Saída: None