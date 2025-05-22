'''
Crie um programa que simula uma calculadora simples. O usuário deve:

Informar dois números,

Escolher uma operação: soma (+), subtração (-), multiplicação (*) ou divisão (/),

O programa exibe o resultado e pergunta se o usuário quer fazer outra operação.

O programa só para quando o usuário digitar "n" para a pergunta “Deseja continuar? (s/n)”.

Use: while, variáveis, entrada e saída de dados, conversão de tipos, e operadores aritméticos.
'''
while True:
    # Entrada de dados
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Escolha a operação (+, -, *, /): ")

    # Processamento
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Erro: divisão por zero.")
            continue
    else:
        print("Operador inválido.")
        continue

    # Saída
    print("Resultado:", resultado)

    # Pergunta se deseja continuar
    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() == "n":
        print("Encerrando a calculadora. Até mais!")
        break
