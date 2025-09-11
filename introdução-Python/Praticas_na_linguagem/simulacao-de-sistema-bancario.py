Menu = """
Bem-vindo ao Sistema Bancário!
Escolha uma opção:

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

saldo = 0.00
limite = 500.00
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(Menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor do depósito deve ser positivo.")

    elif opcao == "2": 
        valor = float(input("Informe o valor do saque: R$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
       
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "0":
        print("Obrigado por usar nosso sistema bancário. Até logo!")
        break

    else:
        print("Operação inválida! Por favor, selecione uma opção válida.")
