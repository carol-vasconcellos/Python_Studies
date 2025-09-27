# contar palavras minusculas do texto

def contar_maiusculas_minusculas(texto):
    contar_maiuscula = 0
    contar_minuscula = 0

    for letra in texto:
        if letra.isupper():
            contar_maiuscula += 1
        elif letra.islower():
            contar_minuscula += 1

    return contar_minuscula, contar_maiuscula

minuscula, maiuscula = contar_maiusculas_minusculas("PyThON")

print(f"Letras maiusculas sao: {minuscula} e maiusculas sao: {maiuscula}")