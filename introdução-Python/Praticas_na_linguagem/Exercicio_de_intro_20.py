'''🎯 Enunciado:

Você está desenvolvendo um sistema para um grupo de estudos com duas turmas: Turma A e Turma B.

    Peça ao usuário os nomes dos alunos da Turma A e da Turma B (sem repetições).

    Armazene os nomes em dois conjuntos.

    Exiba:

        ✅ Alunos que participam das duas turmas.

        🔄 Alunos que estão em apenas uma turma.

        📋 Todos os alunos únicos dos dois grupos.

        ❌ Alunos que estão somente na Turma A.'''

# Entrada de dados
print("Digite os nomes dos alunos da Turma A (separados por vírgula):")
turma_a = set(input().split(","))
turma_a = {nome.strip() for nome in turma_a}

print("\nDigite os nomes dos alunos da Turma B (separados por vírgula):")
turma_b = set(input().split(","))
turma_b = {nome.strip() for nome in turma_b}

# Operações com conjuntos
intersecao = turma_a & turma_b
diferenca_simetrica = turma_a ^ turma_b
uniao = turma_a | turma_b
somente_a = turma_a - turma_b

# Resultados
print("\n✅ Alunos nas duas turmas:", intersecao)
print("🔄 Alunos em apenas uma das turmas:", diferenca_simetrica)
print("📋 Todos os alunos únicos:", uniao)
print("❌ Alunos só da Turma A:", somente_a)
