'''x = {'nome': 'Ana Caroline', 'idade':30, 'cep': '12346789'}

print(x['nome'])'''

#Faça um programa que o usuario possa cadastrar n pessoas, armazenando seu nome, idade e altura

pessoas = []
while True:
    decisao = int(input('Digite 1 para cadastrar uma pessoa e 2 para sair: '))
    if decisao == 2:
        break

    pessoa = {'nome': input('Digite o nome: '),
              'idade': input('Digite a idade: '),
              'altura': input('Digite a altura: ')}

    pessoas.append(pessoa)

print(pessoas)