#Exercício 1 – Número positivo, negativo ou zero Passos lógicos:

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

if a >= b and a >= c:
  print("Numero maior: ", a)
elif b >= a and b >= c:
  print("Numero maior: ", b)
else: 
  print("Numero maior: ", c)


#Exercício 2 – Par ou Ímpar

def even_or_odd(numero):
  
  if numero % 2 == 0:
    print("O número é par")
  else:
    print("O número é impar")

num = int(input("Digite o número: "))
even_or_odd(num)