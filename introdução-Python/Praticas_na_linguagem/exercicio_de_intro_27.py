'''
🧩 Enunciado:

Uma escola decidiu aumentar a nota de todos os alunos em 10%, limitando a nota máxima a 10.0. Você tem uma lista com as notas originais dos alunos. Use a função map() para calcular as novas notas, aplicando o aumento e garantindo que nenhuma ultrapasse 10.
'''

notas = [7.5, 8.0, 9.3, 10.0, 6.8]

notas_atuais = list(map(lambda n: min(n * 1.1, 10.0), notas))

print("Notas atualizadas:", notas_atuais)
