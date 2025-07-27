def cadastrar_usuario(nome, idade):
    return {"nome": nome, "idade": idade}

def listar_usuarios(lista):
    print("\n👥 Usuários Cadastrados:")
    for u in lista:
        print(f"- {u['nome']} ({u['idade']} anos)")
