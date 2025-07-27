x = [{'nome': 'ana', 'idade': 20}, {'nome': 'carol', 'idade': 30}]

x = list(map(lambda x: {'nome': x['nome'], 'idade': 'menor do que 30 anos'} if x['idade'] < 30 else(x), x))

print(x)