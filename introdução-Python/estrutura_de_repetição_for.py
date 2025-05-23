numero = int(input("Digite um número inteiro para ver sua tabuada: "))

print(f"\n📄 Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")