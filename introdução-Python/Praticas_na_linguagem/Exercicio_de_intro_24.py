'''
📘 Enunciado:

Crie um gerador chamado fibonacci(n) que produza os n primeiros números da sequência de Fibonacci.
A sequência de Fibonacci começa assim:
0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Cada número é a soma dos dois anteriores.
'''

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Teste
qtde = int(input("Quantos números da sequência de Fibonacci você quer ver? "))

print("Sequência de Fibonacci:")
for num in fibonacci(qtde):
    print(num)
