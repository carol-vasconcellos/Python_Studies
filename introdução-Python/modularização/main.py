from cadastro import cadastrar_usuario, listar_usuarios
from util import validar_idade

usuarios = []

while True:
    print("\n=== Menu ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome: ")
        idade = None
        while idade is None:
            idade = validar_idade(input("Idade: "))
        usuarios.append(cadastrar_usuario(nome, idade))
    elif opcao == '2':
        listar_usuarios(usuarios)
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
