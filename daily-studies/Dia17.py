# Exercício 1 – Filtrar palavras por tamanho

def palavras_maiores(lista, n):
    return [palavra for palavra in lista if len(palavra) > n]

print(palavras_maiores(["python", "java", "c", "javascript"], 3))

# Exercício 2 – Contagem de caracteres

dicionario = {}

def contagem_caracteres(palavra):
    contagem = {}
    for letra in palavra:
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem

print(contagem_caracteres("python"))

# Exercício 3 – Substituição condicional

def substituir_pares(lista):
    return ["par"
            if x % 2 == 0 
            else x for x in lista]

print(substituir_pares([1, 2, 3, 4, 5]))
    