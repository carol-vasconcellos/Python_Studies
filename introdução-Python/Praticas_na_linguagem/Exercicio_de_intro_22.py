'''
🎯 Enunciado:

Crie uma calculadora que:

    Solicite dois números ao usuário

    Solicite a operação (+, -, *, /)

    Exiba o resultado

    Trate possíveis erros, como:

        Entrada inválida

        Divisão por zero

        Operação inválida
'''

def calcular(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        raise ValueError("Operação inválida!")

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = calcular(a, b, operacao)
    print("✅ Resultado:", resultado)

except ZeroDivisionError:
    print("❌ Erro: divisão por zero não é permitida.")
except ValueError as ve:
    print(f"❌ Erro de valor: {ve}")
except Exception as erro:
    print("❌ Ocorreu um erro inesperado:", erro)
finally:
    print("🧾 Fim do programa.")
