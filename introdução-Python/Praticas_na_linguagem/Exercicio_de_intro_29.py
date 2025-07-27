'''
🎯 Enunciado:

Crie um pequeno sistema em Python que permita:

    Cadastrar vários usuários com as seguintes informações:

        Nome

        Idade

        Email

    Salvar os dados em um arquivo chamado usuarios.pkl usando o módulo pickle.

    Ao iniciar o programa, deve carregar (caso exista) os dados do arquivo e exibi-los.
'''

import pickle
import os

arquivo = 'usuarios.pkl'

# 1. Verificar se o arquivo já existe e carregar dados
if os.path.exists(arquivo):
    with open(arquivo, 'rb') as f:
        usuarios = pickle.load(f)
    print("Usuários carregados do arquivo:")
    for u in usuarios:
        print(f"Nome: {u['nome']}, Idade: {u['idade']}, Email: {u['email']}")
else:
    usuarios = []

# 2. Permitir o cadastro de novos usuários
while True:
    print("\nNovo cadastro:")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    email = input("Email: ")

    usuario = {"nome": nome, "idade": idade, "email": email}
    usuarios.append(usuario)

    continuar = input("Deseja cadastrar outro usuário? (s/n): ").lower()
    if continuar != 's':
        break

# 3. Salvar os dados no arquivo usando pickle
with open(arquivo, 'wb') as f:
    pickle.dump(usuarios, f)

print("\n✅ Dados salvos com sucesso em 'usuarios.pkl'!")
