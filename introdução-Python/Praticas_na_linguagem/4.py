#Exercício 4 – Busca Interativa

#Crie um programa onde:

#O computador tem uma lista de números de 1 a 100.

#O usuário digita um número para procurar.

#O programa usa busca binária para verificar se o número está na lista e mostra a posição

numero = int(input("Digite o número que deseja buscar: "))

lista = list(range(1, 101))

def busca_binaria(lista, alvo):
    baixo = 0 
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == alvo:
            return meio
        if chute > alvo:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None        

resultado = busca_binaria(lista, numero)

if resultado is not None:
    print(f"Número encontrado na posição {resultado + 1}")
else:
    print("Número não encontrado na lista")

