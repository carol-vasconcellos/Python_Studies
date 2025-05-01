''' Peça um valor e uma porcentagem. Calcule e mostre quanto representa essa porcentagem sobre o valor. '''

valor = float(input("Digite um valor: "))
porcentagem = float(input("digite uma porcentagem: "))

porcentagem_sobre_valor = valor * (porcentagem / 100)

print(f"{porcentagem}% de {valor} é {porcentagem_sobre_valor}")