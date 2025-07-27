'''🎯 Enunciado:

Você está criando um sistema simples para registrar livros em uma biblioteca. Cada livro possui:

    Um título.

    Uma lista de edições (ex: primeira edição, segunda edição...).

Faça o seguinte:

    Crie uma lista chamada biblioteca, onde cada livro será representado como uma sublista [título, edições].

    Cadastre 2 livros com 2 edições cada.

    Atribua biblioteca_copia = biblioteca, e depois modifique uma edição em biblioteca_copia.

    Mostre que isso afetou a biblioteca original.

    Agora crie uma cópia real e independente com copy.deepcopy(), e mostre que alterações nessa nova cópia não afetam a original.

    Mostre os id() de cada lista e sublista para comparar os endereços de memória.'''

import copy

# 1. Criar biblioteca
biblioteca = [
    ["Dom Quixote", ["1ª edição", "2ª edição"]],
    ["1984", ["1ª edição", "2ª edição"]],
]

# 2. Atribuição direta (referência)
biblioteca_copia = biblioteca

# 3. Alterar uma edição na cópia
biblioteca_copia[0][1][0] = "1ª edição revisada"

print("📚 Biblioteca original:")
print(biblioteca)
print("\n📚 Biblioteca cópia (referência):")
print(biblioteca_copia)

# 4. Mostrar que ambas foram alteradas
print("\n🔍 IDs de memória (original vs cópia):")
print("id(biblioteca):", id(biblioteca))
print("id(biblioteca_copia):", id(biblioteca_copia))
print("id(biblioteca[0][1]):", id(biblioteca[0][1]))
print("id(biblioteca_copia[0][1]):", id(biblioteca_copia[0][1]))

# 5. Criar cópia independente
biblioteca_segura = copy.deepcopy(biblioteca)
biblioteca_segura[1][1][1] = "2ª edição estendida"

print("\n📚 Biblioteca segura (deepcopy):")
print(biblioteca_segura)

print("\n📚 Biblioteca original (após deepcopy):")
print(biblioteca)

# 6. Ver IDs
print("\n🔍 ID de memória da sublista de edições:")
print("id(biblioteca[1][1]):", id(biblioteca[1][1]))
print("id(biblioteca_segura[1][1]):", id(biblioteca_segura[1][1]))
  