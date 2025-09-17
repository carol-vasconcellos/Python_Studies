# Exercício 1 – Transformar frase em lista de palavras

frase = input("Digite uma frase: ")

palavras = frase.split()
print(palavras)

# Exercício 2 – Contar palavras de uma frase

frase = input("Digite uma frase: ")
palavras = len(frase.split())
print(f"A frase tem {palavras} palavras.")

# Exercício 3 – Substituir vogais por *

frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
resultado = ""

for letra in frase:
    if letra in vogais:
        resultado += "*"
    else:
        resultado += letra

print(resultado)