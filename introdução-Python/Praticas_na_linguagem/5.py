'''Exercício 5 – Desafio Extra 🚀

Implemente um jogo de adivinhação:

O computador escolhe um número secreto entre 1 e 100.

O usuário tenta adivinhar.

O programa dá dicas: "muito alto" ou "muito baixo".

Conte o número de tentativas até acertar.'''

import random

# O computador escolhe o número secreto
numero_secreto = random.randint(1, 100)
tentativas = 0
acertou = False

while not acertou:
    chute = int(input("Adivinhe o número que estou pensando (1 a 100): "))
    tentativas += 1

    if chute == numero_secreto:
        acertou = True
        print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
    elif chute > numero_secreto:
        print("Muito alto!")
    else:
        print("Muito baixo!")
