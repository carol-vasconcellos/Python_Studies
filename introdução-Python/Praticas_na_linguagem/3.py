#Adapte sua função de busca binária para também contar quantos passos foram necessários até achar o número (ou concluir que não existe).

def busca_binaria_com_passos(lista, alvo):
    baixo = 0
    alto = len(lista) - 1
    passos = 0

    while baixo <= alto:
        passos += 1
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == alvo:
            return meio, passos
        if chute > alvo:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None, passos

numeros = [2, 4, 6, 8, 10, 12, 14, 16]
print(busca_binaria_com_passos(numeros, 10))  # Saída
