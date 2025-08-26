class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def retornar_nome(self):
        return self.nome
    
    def logar_sistema(self):
        print(f'{self.retornar_nome()} logado com sucesso!')

p1 = Pessoas('João Augusto', 30)
p2 = Pessoas('Maria Clara', 25)

p1.logar_sistema()