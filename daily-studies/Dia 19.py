# Exercício 1 – Contagem de vogais

def contar_vogais(frase):
    contagem = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
    
    for letra in frase:
        if letra in contagem:   # só conta se for vogal
            contagem[letra] = contagem[letra] + 1
    return contagem

contar = contar_vogais("programacao") 
print(contar)


# Exercício 2 – Intersecção de listas


def intersecao_listas(lista1, lista2):
    intersecao = []
    for item in lista1:
        if item in lista2:
            intersecao.append(item)
    return intersecao

interseccao = intersecao_listas([1, 2, 3, 4], [3, 4, 5, 6]) 

print(interseccao)

# Exercício 3 – Agrupar por inicial

def agrupar_por_inicial(palavras):
    agrupamento = {}

    for palavra in palavras:
        if palavra:
           
            inicial = palavra[0] 
            
            # Se a inicial não existe, cria uma nova lista para ela
            if inicial not in agrupamento:
                agrupamento[inicial] = []
            
            # Adiciona a palavra ao grupo correspondente.
            # Este 'append' deve ser executado para TODOS os casos.
            agrupamento[inicial].append(palavra) 

    return agrupamento

agrupamento = agrupar_por_inicial(["python", "java", "javascript", "c", "csharp"])

print(agrupamento)

# Exercício 4 – Elemento mais frequente

def mais_frequente(lista):
    frequencia = {}

    for item in lista:
        if item in frequencia:
            frequencia[item] += 1
        else:
            frequencia[item] = 1
    return max(frequencia, key=frequencia.get)

frequencia = mais_frequente([1, 2, 2, 3, 3, 3, 4])

print(frequencia)  # Deve imprimir 3

# Exercício 5 – Lista achatada

def lista_achatada(matriz):
    achatada = []

    for lista in matriz:
        for elemento in lista:
            achatada.append(elemento)
    return achatada


achatar = lista_achatada([[1, 2], [3, 4], [5]]) 
# saída: [1, 2, 3, 4, 5]
   
print (achatar)