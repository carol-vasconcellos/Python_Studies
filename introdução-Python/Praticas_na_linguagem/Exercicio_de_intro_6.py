''' Peça o valor de uma compra e o valor pago. Calcule e exiba o troco. '''
valor_compra = float(input("Valor da compra do produto: "))
valor_pago = float(input("Valor pago:"))

troco = (valor_pago - valor_compra)

print(f"O troco recebido é: R$ {troco}")