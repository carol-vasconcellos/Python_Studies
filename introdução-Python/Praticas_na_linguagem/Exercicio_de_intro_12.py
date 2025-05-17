# Calculadora Simples

primeiro = float(input("Digite o primeiro número: "))

segundo = float(input("Digite o segundo número: "))

operador = input("Digite a operação (+, -, *, /): ")

if operador == "+":
    resultado = primeiro + segundo
    print("Resultado: ", resultado)

elif operador == "-":
    resultado = primeiro + segundo
    print("Resultado: ", resultado)

elif operador == "*":
    resultado = primeiro * segundo
    print("Resultado: ", resultado)

elif operador == "/":
    if segundo != 0:
        resultado = primeiro / segundo
        print("Resultado: ", resultado)
    else:
        print("Erro: divisão por zero!")

else:
    print("Operação invalida")