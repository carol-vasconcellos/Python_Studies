# --- Função de verificação (como acima) ---
def verificar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa.")
    assert idade > 0, "Idade deve ser um número inteiro positivo (maior que zero)."
    print("Idade válida!")

# --- Testando e exibindo a saída para cada caso ---

print("--- Teste 1: Idade válida (25) ---")
try:
    verificar_idade(25)
except (ValueError, AssertionError) as e:
    print(f"ERRO INESPERADO: {e}")
print("-" * 30)

print("\n--- Teste 2: Idade negativa (-5) (Esperado: ValueError) ---")
try:
    verificar_idade(-5)
except ValueError as e:
    print(f"SUCESSO! Erro capturado: {e}")
except AssertionError as e:
    print(f"ERRO INESPERADO: {e}")
print("-" * 30)

print("\n--- Teste 3: Idade zero (0) (Esperado: AssertionError) ---")
try:
    verificar_idade(0)
except AssertionError as e:
    print(f"SUCESSO! Erro capturado: {e}")
except ValueError as e:
    print(f"ERRO INESPERADO: {e}")
print("-" * 30)

print("\n--- Teste 4: Idade com tipo errado (string - 'vinte') (Esperado: AssertionError) ---")
try:
    verificar_idade("vinte")
except AssertionError as e:
    print(f"SUCESSO! Erro capturado: {e}")
except ValueError as e:
    print(f"ERRO INESPERADO: {e}")
except TypeError as e: # Captura TypeError que pode ocorrer na comparação idade < 0
    print(f"SUCESSO! Erro capturado (TypeError na comparação): {e}")
print("-" * 30)

print("\n--- Teste 5: Idade com tipo errado (float - 10.5) (Esperado: AssertionError) ---")
try:
    verificar_idade(10.5)
except AssertionError as e:
    print(f"SUCESSO! Erro capturado: {e}")
except ValueError as e:
    print(f"ERRO INESPERADO: {e}")
except TypeError as e: # Captura TypeError que pode ocorrer na comparação idade < 0
    print(f"ERRO INESPERADO: {e}") # Nesse caso, o assert de tipo é mais direto
print("-" * 30)