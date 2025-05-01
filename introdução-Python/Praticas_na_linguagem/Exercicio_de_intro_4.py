'''Peça um valor em reais e a cotação do dólar. Converta e exiba o valor em dólares.'''

valor_real = float(input("Coloque um valor em real: "))
cotacao_do_dolar = float(5.68)

conversao_em_dolar = (valor_real / cotacao_do_dolar) 

print("Valor em dolar: $", round(conversao_em_dolar, 2))