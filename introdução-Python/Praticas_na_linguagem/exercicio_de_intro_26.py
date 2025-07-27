# Dada uma lista de números de 1 a 30, filtre apenas os números primos.

# Dica: crie uma função is_primo(n) que retorna True se o número for primo.
numeros = list(range(1, 31))

def is_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

primos = list(filter(is_primo, numeros))
print("Números primos:", primos)
