'''def minha_funcao():
    soma = 0
    for i in range(0, 101):
        soma = soma + i
    print(soma)

minha_funcao()'''

def soma_valores(n1, n2):
    soma = n1 + n2
    if soma > 5:
        return soma
    
    print("TO AQUI")

soma = soma_valores(5, 2)

print(soma)
