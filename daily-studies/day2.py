#Exercício 1 – Número positivo, negativo ou zero Passos lógicos:

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a => b and a => c:
  print("Numero maior: ", a)
elif b => a and b => c:
  print("Numero maior: ", b)
else: 
  print("Numero maior: ", c)


#Exercício 2 – Par ou Ímpar

numero = int(input("Digite o número: "))

if numero % 2 == 0:
  print("O número é impar")
else:
  print("O número é par")
