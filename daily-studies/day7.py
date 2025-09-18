#Exercício 1 – Função de média

def media (a, b, c):
    return (a + b + c ) /3

print(media(5, 6, 10))

# Exercício 2 – Verificar se número é par

def par(n):
    if n % 2 == 0:
        return True
    else:
        return False
print(par(3))

# Exercício 3 – Calcular fatorial

def fatorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
print(fatorial(5))