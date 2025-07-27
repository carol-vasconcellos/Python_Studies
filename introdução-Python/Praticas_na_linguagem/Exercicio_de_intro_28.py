'''
🧩 Enunciado:

Você recebeu um arquivo chamado alunos.txt contendo o nome dos alunos e três notas de cada um, separados por vírgulas. Exemplo do conteúdo do arquivo:

Ana,7.5,8.0,9.0
Lucas,6.0,7.5,8.5
Carlos,9.0,8.0,10.0

Crie um programa que:

    Leia o arquivo alunos.txt.

    Calcule a média de cada aluno.

    Escreva um novo arquivo chamado medias.txt contendo: nome - média.
'''

with open('alunos.txt', 'r') as entrada:
    linhas = entrada.readlines()

with open('medias.txt', 'w') as saida:
    for linha in linhas:
        dados = linha.strip().split(',')
        nome = dados[0]
        notas = list(map(float, dados[1:]))
        media = sum(notas) / len(notas)
        saida.write(f"{nome} - {round(media, 2)}\n")

print("Arquivo 'medias.txt' gerado com sucesso!")
