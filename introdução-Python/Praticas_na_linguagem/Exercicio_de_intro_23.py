'''
Enunciado:

Crie uma função chamada transferir_saldo que simula uma transferência bancária. Ela deve receber dois argumentos:

    saldo_atual: um número representando o saldo da conta

    valor_transferencia: um número representando o valor que o usuário deseja transferir

A função deve:

    Usar assert para garantir que valor_transferencia seja maior que zero

    Usar raise para lançar uma exceção (ValueError) se o valor da transferência for maior que o saldo disponível

    Retornar o novo saldo após a transferência
'''

def transferir_saldo(saldo_atual, valor_transferencia):
    assert valor_transferencia > 0, "O valor da transferência deve ser positivo."

    if valor_transferencia > saldo_atual:
        raise ValueError("Saldo insuficiente para a transferência.")

    return saldo_atual - valor_transferencia


# Testes:
try:
    novo_saldo = transferir_saldo(1000, 300)
    print("✅ Transferência concluída. Novo saldo:", novo_saldo)

    novo_saldo = transferir_saldo(700, -50)  # Deve disparar o assert
    print("✅ Novo saldo:", novo_saldo)

except AssertionError as e:
    print("⚠️ Erro de validação:", e)

except ValueError as e:
    print("❌ Erro de saldo:", e)
