num_alunos = int(input("Quantos alunos deseja cadastrar? "))

alunos = []

for _ in range(num_alunos):
    nome = input("\nDigite o nome do aluno: ")
    notas = []
    for i in range(4):
        nota = float(input(f"Digite a nota {i+1}: "))
        notas.append(nota)
    
    media = sum(notas) / 4
    alunos.append([nome, notas, media])

# Mostrar dados de cada aluno
print("\n---- Lista de alunos e médias ----")
for aluno in alunos:
    nome, notas, media = aluno
    print(f"Aluno: {nome} | Notas: {notas} | Média: {media:.2f}")

# Encontrar maior média
maior_media = max(alunos, key=lambda x: x[2])
print(f"\nAluno com maior média: {maior_media[0]} ({maior_media[2]:.2f})")

# Calcular média geral
media_geral = sum(aluno[2] for aluno in alunos) / num_alunos
print(f"Média geral da turma: {media_geral:.2f}")

# Contar aprovados e reprovados
aprovados = sum(1 for aluno in alunos if aluno[2] >= 7)
reprovados = num_alunos - aprovados

print(f"Quantidade de alunos aprovados: {aprovados}")
print(f"Quantidade de alunos reprovados: {reprovados}")
