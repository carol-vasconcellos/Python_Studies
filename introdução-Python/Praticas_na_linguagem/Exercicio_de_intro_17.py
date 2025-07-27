alunos = int(input("Quantos alunos? "))
provas = int(input("Quantas provas por aluno? "))

matriz = []

# Entrada de dados
for i in range(alunos):
    linha = []
    print(f"\nAluno {i+1}")
    for j in range(provas):
        nota = float(input(f"Nota da prova {j+1}: "))
        linha.append(nota)
    matriz.append(linha)

# Mostrar matriz
print("\n📋 Matriz de notas:")
for linha in matriz:
    for nota in linha:
        print(f"{nota:.1f}", end="\t")
    print()

# Média de cada aluno
print("\n📈 Média de cada aluno:")
for i in range(alunos):
    media = sum(matriz[i]) / provas
    print(f"Aluno {i+1}: Média = {media:.2f}")

# Média de cada prova (coluna)
print("\n📊 Média de cada prova:")
for j in range(provas):
    soma = 0
    for i in range(alunos):
        soma += matriz[i][j]
    media = soma / alunos
    print(f"Prova {j+1}: Média = {media:.2f}")

# Encontrar maior e menor nota
maior = matriz[0][0]
menor = matriz[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

for i in range(alunos):
    for j in range(provas):
        nota = matriz[i][j]
        if nota > maior:
            maior = nota
            pos_maior = (i, j)
        if nota < menor:
            menor = nota
            pos_menor = (i, j)

print(f"\n🔝 Maior nota: {maior:.1f} (Aluno {pos_maior[0]+1}, Prova {pos_maior[1]+1})")
print(f"🔻 Menor nota: {menor:.1f} (Aluno {pos_menor[0]+1}, Prova {pos_menor[1]+1})")
