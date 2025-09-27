# contar palavras

def contar_palavras(frase):
    contidade_letras = len(frase.split())
    return contidade_letras


print(contar_palavras("O rato roeu a roupa do rei de roma"))


# retornar a maior palavra

'''numa lista de strings, deve usar a função max() com o argumento key=len para encontrar a string mais longa, ou pode determinar a "maior palavra"'''

def maior_palavra(lista_palavras):
    maior_palavra = max(lista_palavras, key=len)
    return maior_palavra


print(maior_palavra(["python", "java", "javascript"]))