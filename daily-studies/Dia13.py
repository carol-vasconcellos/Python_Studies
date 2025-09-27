# Verifcar se e palindromo

def palindromo(palavra):
    texto_processado = "".join(palavra.split()).lower()

    texto_invertido = texto_processado[::-1]

    return texto_processado == texto_invertido

print(palindromo("arara"))

# subistituir espaço *replace()*

def substituir_espacos(frase):
    sub = frase.replace(" ", "-")

    return sub

print(substituir_espacos("Olá mundo com espaços"))