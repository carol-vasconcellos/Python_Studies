''' Receba o peso (kg) e a altura (m) do usuário. Calcule e mostre o IMC. '''

peso = float(input(" Digite seu peso: "))
altura = float(input(" Digite sua altura: "))

imc = (peso / altura ** 2)

print(' Seu IMC é:', round(imc, 2))
