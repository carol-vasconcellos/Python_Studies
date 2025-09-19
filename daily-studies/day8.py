# Exercício 1 – Contar vogais
def contar_vogais(palavra):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador
print(contar_vogais("Hello World"))

# Exercício 2 – Soma de números pares em lista

def soma_pares(lista):
    soma = []
    for numero in lista:
        if numero % 2 == 0:
            soma.append(numero)
    return sum(soma)

print(soma_pares([1, 2, 3, 4, 5, 6]))

# Exercício 3 – Reverter palavras de uma frase

def reverter(frase):
    palavras = frase.split()
    palavras_revertidas = palavras[::-1]
    return ' '.join(palavras_revertidas)

print(reverter("Hello World from Python"))

