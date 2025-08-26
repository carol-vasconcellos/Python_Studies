class Pessoas:
    possui_olho = True
    possui_boca = True
    raca = 'Humano'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retornar_nome(self):
        return self.nome
    
    def logar_sistema(self):
        print(f'{self.retornar_nome()} logado com sucesso!')

# Exemplo de atributos de classe
p1 = Pessoas('João', 30)
p2 = Pessoas('Maria', 25)

print(p1.possui_boca)
print(p2.possui_olho)