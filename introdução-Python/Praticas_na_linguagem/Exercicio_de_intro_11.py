# 1. Usando AND
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")  # ✅
else:
    print("Não pode dirigir.")

# 2. Usando OR
tem_ingresso = False
nome_na_lista = True

if tem_ingresso or nome_na_lista:
    print("Pode entrar.")  # ✅
else:
    print("Entrada negada.")

# 3. Usando NOT
chovendo = False

if not chovendo:
    print("Pode sair sem guarda-chuva.")  # ✅
else:
    print("Leve um guarda-chuva.")