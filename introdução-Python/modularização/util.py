def validar_idade(valor):
    try:
        idade = int(valor)
        if idade > 0:
            return idade
        else:
            print("Idade deve ser positiva.")
            return None
    except ValueError:
        print("Idade inválida. Digite um número.")
        return None
