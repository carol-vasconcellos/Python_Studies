arquivo = open('pessoas.txt', 'w')
resultados = arquivo.readlines()

x = []
for i in resultados:
    x.append(i.split())
print(x[1][1])
arquivo.close()