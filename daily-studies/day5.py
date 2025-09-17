# Exercício 1 – Contar vogais em uma palavra

texto = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
contador = 0

for letra in texto:
    if letra in vogais:
        contador += 1

print(f"A palavra '{texto}' tem {contador} vogais.")
    
# Exercício 2 – Verificar palíndromo( colocando a palavra de trás para frente e ela ter a mesma leitura)

palavra = input("Digite uma palavra: ").lower()
if texto == texto[::-1]:
    print(f"A palavra '{palavra}' é um palíndromo.")    
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")    

