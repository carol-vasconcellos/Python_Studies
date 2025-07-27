import pickle

class Pessoa:
    nome = 'ana'
    idade = 20

arq = open('arquivo.pkl', 'wb')
pickle.dump(Pessoa, arq)

arq = open('arquivo.pkl', 'rb')
retornou = pickle.load(arq)

print(retornou.idade)