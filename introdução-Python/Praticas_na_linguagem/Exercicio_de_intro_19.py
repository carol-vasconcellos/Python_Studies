produtos = []

for i in range(3):
    print(f"\nCadastro do produto {i+1}")
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

# Produto mais caro
mais_caro = max(produtos, key=lambda p: p["preco"])
print(f"\n🤑 Produto mais caro: {mais_caro['nome']} - R$ {mais_caro['preco']:.2f}")

# Total do estoque
valor_total = 0
print("\n📦 Produtos e valor total individual:")
for p in produtos:
    total_individual = p["preco"] * p["quantidade"]
    valor_total += total_individual
    print(f"- {p['nome']}: R$ {p['preco']} × {p['quantidade']} = R$ {total_individual:.2f}")

print(f"\n💰 Valor total de todos os produtos no estoque: R$ {valor_total:.2f}")
