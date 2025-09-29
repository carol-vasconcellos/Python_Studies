# Exercício 1 – Frequência de palavras

def contar_palavras(frase):
    contagem = {}

    for letra in frase.split():
        if letra in contagem:
            contagem[letra] += 1
        else:
            contagem[letra] = 1
    return contagem
    
print(contar_palavras("o rato roeu a roupa do rei de roma o rato"))

# Exercício 2 – Remover duplicados

def remover_duplicados(lista):
    nova_lista = []

    for list in lista:
        if list not in nova_lista:
            nova_lista.append(list)
    return nova_lista

remover = remover_duplicados([1, 2, 2, 3, 1, 4, 4, 5])

print(remover)

# Exercício 3 – Maior palavra por inicial

def maior_palavra_por_inicial(lista):
    resultado = {}

    for palavra in lista:
        inicial = palavra[0]
        if inicial not in resultado:
            resultado[inicial] = palavra
        else:
            if len(palavra) > len(resultado[inicial]):
                resultado[inicial] = palavra
    return resultado


maior = maior_palavra_por_inicial(["python", "java", "javascript", "c", "csharp"])

print(maior)