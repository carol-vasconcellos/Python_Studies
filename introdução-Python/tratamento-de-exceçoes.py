'''n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))

try:  #tente
    print(n1/n2)
except: # se não conseguir
    print('Não consegui')
finally:
    print('Finalizado!')'''

try:
    x = int(input('Digite um numero: '))
    print(5/x)
except ValueError:
    print('Digite um numero inteiro!')
except ZeroDivisionError:
    print('Não digite 0!')