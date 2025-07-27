''' 🎯 Enunciado:

Crie um sistema de cadastro de alunos usando funções.

1. Crie uma função `cadastrar_aluno` que recebe **nome, idade e curso** e retorna um **dicionário** com esses dados.
2. Crie uma função `exibir_alunos` que recebe uma **lista de alunos** e imprime todos de forma formatada.
3. Permita o cadastro de **vários alunos** usando um laço.
4. Ao final, exiba a lista completa dos alunos cadastrados.
'''

def cadastrar_aluno(nome, idade, curso):
    return {
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

def exibir_alunos(lista_alunos):
    print("\n📋 Lista de Alunos Cadastrados:")
    for aluno in lista_alunos:
        print(f"- {aluno['nome']} ({aluno['idade']} anos) - Curso: {aluno['curso']}")

# Lista para armazenar os alunos
alunos = []

while True:
    print("\n--- Cadastro de Aluno ---")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    curso = input("Curso: ")

    aluno = cadastrar_aluno(nome, idade, curso)
    alunos.append(aluno)

    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if continuar != 's':
        break