# Python_Studies

## *Índice*

- [Introdução](#introdução)
- [Variáveis](#variáveis)
- [Tipos de dados](#tipos-de-dados)
- [Entrada e Saída de Dados](#entrada-e-saída-de-dados)
- [Conversão de Dados](#conversão-de-dados)
- [Operadores Aritméticos](#operadores-aritméticos)
- [Operadores Lógicos](#operadores-lógicos)
- [Estrutura de Decisão](#estrutura-de-decisão)
- [🧠 Estrutura de Repetição while](#-estrutura-de-repetição-while)
- [🧠 Estrutura de Repetição for](#-estrutura-de-repetição-for)
- [🧠 Laço for e Complexidade Algorítmica](#-laço-for-e-complexidade-algorítmica)
- [🧠 O que são listas em Python?](#-o-que-são-listas-em-python)
- [🧠 O que são listas de listas (matrizes) em Python?](#-o-que-são-listas-de-listas-matrizes-em-python)
- [🧠 O que é referência de memória em Python?](#-o-que-é-referência-de-memória-em-python)
- [🧠 O que são dicionários?](#-o-que-são-dicionários)
- [🧠 O que são Conjuntos?](#-o-que-são-conjuntos)
- [🧠 O que são funções?](#-o-que-são-funções)
- [🧠 O que é Modularização?](#-o-que-é-modularização)
- [🧠 O que é Tratamento de Exceções?](#-o-que-é-tratamento-de-exceções)
- [Geradores em Python — explicação e exercício](#geradores-em-python--explicação-e-exercício)
- [⚡ O que é uma função lambda?](#-o-que-é-uma-função-lambda)
- [🧪 O que é filter()?](#-o-que-é-filter)
- [🧠 O que é map()?](#-o-que-é-map)
- [📂 Trabalhando com Arquivos em Python](#-trabalhando-com-arquivos-em-python)


 ESSE DIRETORIO AJUDARÁ NO CONHECIMENTO DA LINGUAGEM PYTHON


> 📌 Obs: No GitHub, os títulos `## Título` viram automaticamente âncoras com base nas regras mencionadas. Se tiver dúvida sobre a âncora correta, clique no ícone de link ao lado do título no próprio GitHub.

Quer que eu gere um índice automático com base em um README que você já tem?

## Introdução

**Faça um ambiente virtual:** python3 -m venv venv
**Entrar no ambiente virtual:** source venv/bin/activate ( Linux ) -  "venv"\Scripts\activate.bat ( windows )

### Variáveis

Variáveis são "nomes" que guardam valores na memória para serem usados no programa. Elas servem para armazenar dados como números, textos, listas, etc.

#### 📌 Como funciona em Python:
Você cria uma variável atribuindo um valor a um nome com o sinal `=`.

```python
nome = "Ana"
idade = 25
preco = 10.99
```

#### 🧠 Exemplo prático:
```python
mensagem = "Olá, mundo!"
print(mensagem)
```
> Aqui, `mensagem` guarda o texto "Olá, mundo!" e o `print` mostra esse conteúdo.

#### 💡 Dica:
- Você **não precisa declarar o tipo** (como `int` ou `string`) em Python — ele entende automaticamente.
- Nomes de variáveis devem ser simples e claros: `total_pontos`, `nome_usuario`, etc.

### Tipos de dados

São as categorias dos valores que uma variável pode guardar. Cada tipo define o que o valor representa e o que você pode fazer com ele.

#### 🔹 Tipos principais:

1. **`int` (inteiro)** → Números sem casas decimais  
   Ex: `idade = 30`, `pontos = -5`

2. **`float` (decimal)** → Números com casas decimais  
   Ex: `altura = 1.75`, `preco = 9.99`

3. **`str` (string)** → Texto  
   Ex: `nome = "Maria"`, `mensagem = "Olá!"`

4. **`bool` (booleano)** → Verdadeiro ou falso  
   Ex: `ativo = True`, `conectado = False`

5. **`list` (lista)** → Conjunto de valores organizados  
   Ex: `frutas = ["maçã", "banana", "uva"]`

6. **`dict` (dicionário)** → Pares chave:valor  
   Ex: `usuario = {"nome": "João", "idade": 25}`

7. **`tuple` (tupla)** → Lista imutável  
   Ex: `coordenadas = (10, 20)`

8. **`set` (conjunto)** → Conjunto sem itens repetidos  
   Ex: `numeros = {1, 2, 3}`

#### 🧠 Exemplo prático:
```python
nome = "Lucas"
idade = 28
altura = 1.80
ativo = True
hobbies = ["ler", "jogar", "correr"]
```

> Aqui temos `str`, `int`, `float`, `bool` e `list` em ação.

### Entrada e Saída de Dados 

A **entrada** pega dados do usuário; a **saída** mostra algo na tela. O `f""` é usado para **formatar strings**, ou seja, misturar texto com variáveis de forma simples e elegante.

---

#### 🔹 Saída com `f""` (f-strings)
Permite mostrar variáveis dentro de um texto de forma clara:

```python
nome = "Ana"
idade = 20
print(f"Olá, {nome}! Você tem {idade} anos.")
```

> Resultado: `Olá, Ana! Você tem 20 anos.`

---

#### 🔹 Entrada com `input()`
Pede que o usuário digite algo:

```python
nome = input("Digite seu nome: ")
print(f"Bem-vinda, {nome}!")
```

> Se o usuário digitar `Maria`, a saída será: `Bem-vinda, Maria!`

---

#### 🔹 Conversão de tipos com entrada
Por padrão, `input()` retorna **string**, então convertemos quando for número:

```python
idade = int(input("Digite sua idade: "))
print(f"Daqui a 10 anos, você terá {idade + 10} anos.")
```



#### ✅ Resumo rápido:
- `input()` → recebe dados do usuário.
- `print()` → mostra dados na tela.
- `f""` → insere variáveis direto no texto (formatação moderna e clara).

---

### Conversão de Dados
É o processo de **transformar um tipo de dado em outro**, como texto em número, número em texto, etc. Isso é útil quando precisamos fazer operações específicas (como somar números que vieram como string).

#### 🔹 Conversões mais comuns:

1. **`int()`** → Converte para inteiro  
   Ex: `int("10")` → `10`

2. **`float()`** → Converte para decimal  
   Ex: `float("3.14")` → `3.14`

3. **`str()`** → Converte para string (texto)  
   Ex: `str(25)` → `"25"`

4. **`bool()`** → Converte para verdadeiro/falso  
   Ex: `bool(0)` → `False`, `bool("texto")` → `True`

#### 🧠 Exemplos práticos:

```python
# Convertendo entrada para número
idade = int(input("Digite sua idade: "))
print(f"Daqui a 5 anos, você terá {idade + 5} anos.")

# Convertendo número para texto
numero = 100
mensagem = "O valor é " + str(numero)
print(mensagem)

# Convertendo texto para float
preco = float("9.99")
```

#### ⚠️ Cuidado:
Se tentar converter algo que não faz sentido, dá erro:
```python
int("abc")  # ❌ erro: não é um número
```

#### 🔹 Exemplo com `type()`:

```python
nome = "Ana"
idade = 30
altura = 1.65
ativo = True

print(type(nome))     # <class 'str'>
print(type(idade))    # <class 'int'>
print(type(altura))   # <class 'float'>
print(type(ativo))    # <class 'bool'>
```

#### ✅ Diferença:

| Função     | Faz o quê?                              |
|------------|------------------------------------------|
| `int()`, `float()`, `str()` etc. | **Convertem** dados de um tipo para outro |
| `type()`   | **Informa** qual é o tipo atual de um dado |

---

### Operadores Aritméticos   
São símbolos que servem para fazer **contas matemáticas** como somar, subtrair, multiplicar, dividir, etc.

#### 🔹 Principais operadores:

| Operador | Significado        | Exemplo           | Resultado |
|----------|--------------------|-------------------|-----------|
| `+`      | Soma               | `2 + 3`           | `5`       |
| `-`      | Subtração          | `5 - 2`           | `3`       |
| `*`      | Multiplicação      | `4 * 3`           | `12`      |
| `/`      | Divisão (float)    | `10 / 2`          | `5.0`     |
| `//`     | Divisão inteira    | `10 // 3`         | `3`       |
| `%`      | Resto da divisão   | `10 % 3`          | `1`       |
| `**`     | Potência (expoente)| `2 ** 3`          | `8`       |

### 🧠 Exemplos práticos:

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

### 💡 Dica:
Você pode usar esses operadores dentro de `print()`, com variáveis ou valores diretos.


### **Operadores Relacionais (em Python)**
Também chamados de **operadores de comparação**, eles comparam valores e retornam um **booleano**: `True` (verdadeiro) ou `False` (falso).

---

#### 🔹 Tabela de operadores:

| Operador | Significado      | Exemplo  | Resultado |
| -------- | ---------------- | -------- | --------- |
| `==`     | Igual a          | `5 == 5` | `True`    |
| `!=`     | Diferente de     | `5 != 3` | `True`    |
| `>`      | Maior que        | `7 > 4`  | `True`    |
| `<`      | Menor que        | `3 < 8`  | `True`    |
| `>=`     | Maior ou igual a | `6 >= 6` | `True`    |
| `<=`     | Menor ou igual a | `2 <= 5` | `True`    |

---

#### 🧠 Exemplo prático:

```python
idade = 18
print(idade >= 18)  # True (é maior ou igual a 18)
print(idade == 21)  # False
```

---

#### 💡 Usados em:

* **condições** (`if`, `while`)
* **filtros** em listas
* **validações** de entrada do usuário

```python
senha = input("Digite a senha: ")
print(senha == "1234")  # True se for a senha certa
```

#### **exemplos práticos** usando **operadores relacionais**:

##### ✅ 1. Comparando idades:

```python
idade = 20

print(idade == 20)   # True
print(idade != 18)   # True
print(idade > 18)    # True
print(idade < 25)    # True
print(idade >= 21)   # False
print(idade <= 20)   # True
```

---

##### ✅ 2. Validação simples com `input`:

```python
senha = input("Digite a senha: ")

if senha == "abc123":
    print("Acesso permitido!")
else:
    print("Senha incorreta.")
```

---

##### ✅ 3. Usando operadores relacionais com condições:

```python
nota = float(input("Digite sua nota: "))

if nota >= 7.0:
    print("Aprovado!")
else:
    print("Reprovado.")
```

---

##### ✅ 4. Comparando dois números:

```python
a = 5
b = 10

print(a < b)    # True
print(a > b)    # False
print(a == b)   # False
```

---

### **Operadores Lógicos**
São usados para **combinar condições**. Eles retornam `True` ou `False` com base no resultado das expressões.


#### 🔹 Tabela de operadores:

| Operador | Significado               | Exemplo          | Resultado |
| -------- | ------------------------- | ---------------- | --------- |
| `and`    | E (tudo precisa ser True) | `True and False` | `False`   |
| `or`     | OU (basta um ser True)    | `True or False`  | `True`    |
| `not`    | NÃO (inverte o valor)     | `not True`       | `False`   |

---

#### 🧠 Exemplos práticos:

```python
# 1. Usando AND
idade = 20
tem_carteira = True

if idade >= 18 and tem_carteira:
    print("Pode dirigir.")  # ✅
else:
    print("Não pode dirigir.")

# 2. Usando OR
tem_ingresso = False
nome_na_lista = True

if tem_ingresso or nome_na_lista:
    print("Pode entrar.")  # ✅
else:
    print("Entrada negada.")

# 3. Usando NOT
chovendo = False

if not chovendo:
    print("Pode sair sem guarda-chuva.")  # ✅
else:
    print("Leve um guarda-chuva.")
```

---

#### 💡 Dica rápida:

* `and`: só dá `True` se **todas** as condições forem verdadeiras.
* `or`: dá `True` se **qualquer uma** for verdadeira.
* `not`: **inverte** o resultado lógico.

---

### **Estrutura de Decisão**

Serve para **tomar decisões** com base em condições. Usa-se principalmente o `if`, `elif` e `else`.

---

#### 🔹 Sintaxe básica:

```python
if condição:
    # código se for verdadeiro
elif outra_condição:
    # código se a outra for verdadeira
else:
    # código se nenhuma for verdadeira
```

---

#### 🧠 Exemplos práticos:

##### ✅ Exemplo 1: Verificando idade

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade.")
else:
    print("Menor de idade.")
```

---

##### ✅ Exemplo 2: Nota do aluno

```python
nota = float(input("Digite a nota: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

---

##### ✅ Exemplo 3: Par ou ímpar

```python
numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")
```

---

#### 💡 Dica:

Você pode **combinar com operadores lógicos e relacionais**:

```python
if idade >= 18 and idade <= 60:
    print("Adulto em idade ativa")
```

---

### 🧠 Estrutura de Repetição `while`

#### 🔁 O que é o `while`?

A estrutura `while` executa um bloco de código **enquanto** uma condição for **verdadeira**.

#### 📌 Sintaxe:

```python
while condição:
    # bloco de código
```

O Python vai **verificar a condição**:

* Se for `True` (verdadeira), ele executa o bloco e **volta a checar**.
* Se for `False`, ele **para** e segue para o código após o `while`.

---

#### 🛑 Exemplo simples:

```python
contador = 0

while contador < 5:
    print("Contando:", contador)
    contador += 1
```

**Saída:**

```
Contando: 0
Contando: 1
Contando: 2
Contando: 3
Contando: 4
```

A repetição para quando `contador` chega a 5.

---

#### 🧩 Exercício 1 – Calculadora simples com `while`

##### 📋 Enunciado:

Crie um programa que simula uma calculadora simples. O usuário deve:

* Informar dois números,
* Escolher uma operação: soma (`+`), subtração (`-`), multiplicação (`*`) ou divisão (`/`),
* O programa exibe o resultado e pergunta se o usuário quer fazer outra operação.
* O programa só para quando o usuário digitar `"n"` para a pergunta “Deseja continuar? (s/n)”.

> **Use:** `while`, variáveis, entrada e saída de dados, conversão de tipos, e operadores aritméticos.

---


Perfeito! Agora vamos falar da estrutura de repetição `**for**` em Python — explicação clara e um exercício completo com todos os temas misturados, assim como no caso do `while`. 🚀

---

### 🧠  Estrutura de Repetição `for`

#### 🔁 O que é o `for`?

A estrutura `for` é usada para **repetir um bloco de código um número conhecido de vezes**, **percorrer listas, strings ou intervalos numéricos**.

#### 📌 Sintaxe com `range()`:

```python
for variável in range(início, fim, passo):
    # bloco de código
```

* `início` → valor inicial (inclusivo)
* `fim` → valor final (exclusivo)
* `passo` → incremento (opcional, padrão é 1)

---

#### 🛠 Exemplo:

```python
for i in range(1, 6):
    print("Contando:", i)
```

**Saída:**

```
Contando: 1
Contando: 2
Contando: 3
Contando: 4
Contando: 5
```

---

### 🧩 Exercício 2 – Tabuada com `for`

#### 📋 Enunciado:

Crie um programa que:

* Peça ao usuário um número inteiro,
* Mostre a **tabuada desse número de 1 a 10** usando `for`.

> **Use:** `for`, variáveis, entrada/saída, conversão de dados e operadores aritméticos.

---

#### ✅ Código proposto:

```python
numero = int(input("Digite um número inteiro para ver sua tabuada: "))

print(f"\n📄 Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

---

#### 🎯 O que esse exercício pratica:

* ✅ Variáveis (`numero`, `i`, `resultado`)
* ✅ Tipos de dados (`int`)
* ✅ Entrada/saída (`input`, `print`)
* ✅ Conversão (`int(input())`)
* ✅ Operadores aritméticos (`*`)
* ✅ Estrutura de repetição com `for` e `range()`

---

### 🧠 **Laço `for` e Complexidade Algorítmica**

Já sabemos que o O laço `for` permite repetir um trecho de código **um número determinado de vezes**, sendo muito usado para percorrer estruturas como `range()`, listas, strings, etc. Junto  a **complexidade algorítmica** indica **quanto tempo (tempo de execução)** ou **quantos recursos (memória)** um algoritmo consome em função da entrada.
É expressa usando a **notação Big-O** (`O(...)`), que mostra o **comportamento em escala**.

---

#### 📊 Exemplos de complexidade com `for`

##### 🔹 `O(1)` – Tempo constante:

```python
print("Olá")  # Executa uma vez, sempre.
```

##### 🔹 `O(n)` – Linear:

```python
for i in range(n):
    print(i)  # Executa n vezes
```

> O tempo cresce **proporcional ao tamanho da entrada**.

##### 🔹 `O(n²)` – Quadrática:

```python
for i in range(n):
    for j in range(n):
        print(i, j)  # Executa n * n vezes
```

> Muito comum em algoritmos de comparação, como **bubble sort**.

##### 🔹 `O(n³)` – Cúbica:

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```

> Raramente ideal. Escala muito mal.

##### 🔹 `O(log n)` – Logarítmica:

```python
i = 1
while i < n:
    print(i)
    i *= 2
```

> Cada passo dobra, logo poucos passos mesmo para entradas grandes.

##### 🔹 `O(n log n)` – Linearítmica:

> Ocorre em algoritmos eficientes de ordenação, como **Merge Sort**.


#### ✅ Dicas:

* Use o `for` com consciência: loops aninhados aumentam a complexidade.
* Em grandes dados, **prefira algoritmos `O(n log n)` ou menores**.
* Entenda a diferença entre **quantidade de laços** e **quantidade de trabalho feito**.

---

## 🧠 O que são **listas** em Python?

### 📦 Lista = coleção ordenada de elementos (valores)

Você pode guardar **vários dados juntos**, inclusive de tipos diferentes.

```python
numeros = [1, 2, 3, 4, 5]
nomes = ["Ana", "João", "Lucas"]
```

---

### 🔧 Ações comuns com listas:

| Ação                  | Exemplo                    |
| --------------------- | -------------------------- |
| Acessar elemento      | `lista[0]`                 |
| Alterar elemento      | `lista[1] = 99`            |
| Adicionar no final    | `lista.append(10)`         |
| Inserir em posição    | `lista.insert(2, 33)`      |
| Remover por valor     | `lista.remove(33)`         |
| Remover por índice    | `lista.pop(0)`             |
| Tamanho da lista      | `len(lista)`               |
| Percorrer com `for`   | `for item in lista:`       |
| Ordenar (crescente)   | `lista.sort()`             |
| Ordenar (decrescente) | `lista.sort(reverse=True)` |

---

## 🧩 Exercícios com Listas

---

### 🔹 **Exercício 1 – Soma de uma lista de números**

**Enunciado:**
Peça ao usuário para digitar 5 números. Armazene em uma lista. Depois, calcule e mostre a soma total.

```python
numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

soma = sum(numeros)
print("A soma dos números é:", soma)
```

---

### 🔹 **Exercício 2 – Encontrar o maior número da lista**

**Enunciado:**
Receba 5 números e mostre o **maior valor** entre eles.

```python
numeros = []

for i in range(5):
    num = float(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

maior = max(numeros)
print("O maior número digitado foi:", maior)
```

---

### 🔹 **Exercício 3 – Contar números pares**

**Enunciado:**
Peça uma quantidade de números e conte quantos deles são pares.

```python
quant = int(input("Quantos números deseja digitar? "))
pares = 0

for i in range(quant):
    num = int(input("Digite um número: "))
    if num % 2 == 0:
        pares += 1

print(f"Você digitou {pares} número(s) par(es).")
```

---

### 🔹 **Exercício 4 – Lista invertida**

**Enunciado:**
Peça 5 nomes ao usuário, armazene-os e mostre em **ordem reversa**.

```python
nomes = []

for i in range(5):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)

print("Nomes em ordem reversa:")
for nome in reversed(nomes):
    print(nome)
```

---

### 🔹 **Exercício 5 – Média com lista**

**Enunciado:**
Peça ao usuário quantas notas quer inserir. Armazene em uma lista e mostre a média final.

```python
notas = []
quant = int(input("Quantas notas deseja digitar? "))

for i in range(quant):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print("Média das notas:", round(media, 2))
```

---

### 🔹 **Exercício 6 – Buscar um valor**

**Enunciado:**
Peça uma lista de números ao usuário e pergunte por um valor. Diga se ele está ou não na lista.

```python
numeros = []
for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)

busca = int(input("Qual número deseja buscar? "))

if busca in numeros:
    print("Número encontrado!")
else:
    print("Número NÃO encontrado.")
```

---

### 🔹 **Exercício 7 – Remover valor repetido**

**Enunciado:**
Receba uma lista de números. Remova todas as **ocorrências duplicadas**, mantendo apenas um de cada.

```python
numeros = []

for i in range(6):
    num = int(input("Digite um número: "))
    numeros.append(num)

# Usar set para remover duplicatas e voltar para lista
sem_repeticao = list(set(numeros))

print("Lista sem repetição:", sem_repeticao)
```

---

### 🔹 **Exercício 8 – Lista de quadrados**

**Enunciado:**
Receba 5 números e crie uma nova lista com o **quadrado de cada número**.

```python
numeros = []
quadrados = []

for i in range(5):
    num = int(input("Digite um número: "))
    numeros.append(num)
    quadrados.append(num ** 2)

print("Números:", numeros)
print("Quadrados:", quadrados)
```

---

## 🧠 O que são **listas de listas** (matrizes) em Python?

Uma **matriz** em Python é representada como uma **lista que contém outras listas**. Exemplo de uma matriz 3x3 (3 linhas, 3 colunas):

```python
matriz = [
    [1, 2, 3],   # Linha 0
    [4, 5, 6],   # Linha 1
    [7, 8, 9]    # Linha 2
]
```

* `matriz[0][1]` → Acessa o valor `2`
* `matriz[2][0]` → Acessa o valor `7`

---

## 🔁 Como percorrer uma matriz com `for`

```python
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()  # Quebra de linha a cada nova linha da matriz
```

---

## 🧩 Exercício Completo – Matriz de Notas e Estatísticas

### 📋 Enunciado:

Crie um programa que:

1. Peça ao usuário quantos alunos e quantas provas cada um terá.
2. Monte uma matriz onde:

   * Cada **linha representa um aluno**.
   * Cada **coluna representa a nota daquela prova**.
3. Depois, o programa deve:

   * Calcular e exibir a **média de cada aluno**.
   * Calcular a **média de cada prova (coluna)**.
   * Mostrar a **maior e menor nota da matriz**, com suas posições (linha e coluna).

---

### ✅ Código exemplo:

```python
alunos = int(input("Quantos alunos? "))
provas = int(input("Quantas provas por aluno? "))

matriz = []

# Entrada de dados
for i in range(alunos):
    linha = []
    print(f"\nAluno {i+1}")
    for j in range(provas):
        nota = float(input(f"Nota da prova {j+1}: "))
        linha.append(nota)
    matriz.append(linha)

# Mostrar matriz
print("\n📋 Matriz de notas:")
for linha in matriz:
    for nota in linha:
        print(f"{nota:.1f}", end="\t")
    print()

# Média de cada aluno
print("\n📈 Média de cada aluno:")
for i in range(alunos):
    media = sum(matriz[i]) / provas
    print(f"Aluno {i+1}: Média = {media:.2f}")

# Média de cada prova (coluna)
print("\n📊 Média de cada prova:")
for j in range(provas):
    soma = 0
    for i in range(alunos):
        soma += matriz[i][j]
    media = soma / alunos
    print(f"Prova {j+1}: Média = {media:.2f}")

# Encontrar maior e menor nota
maior = matriz[0][0]
menor = matriz[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

for i in range(alunos):
    for j in range(provas):
        nota = matriz[i][j]
        if nota > maior:
            maior = nota
            pos_maior = (i, j)
        if nota < menor:
            menor = nota
            pos_menor = (i, j)

print(f"\n🔝 Maior nota: {maior:.1f} (Aluno {pos_maior[0]+1}, Prova {pos_maior[1]+1})")
print(f"🔻 Menor nota: {menor:.1f} (Aluno {pos_menor[0]+1}, Prova {pos_menor[1]+1})")
```

---

### ✅ O que você pratica aqui:

* Listas de listas (matriz)
* Entrada de dados com `input`
* Conversão com `float`
* Laços `for` aninhados
* Operadores aritméticos (soma, comparação)
* Organização de dados tabular
* Lógica para busca de valores máximos e mínimos
* Compreensão de linhas e colunas

---

## 🧠 O que é **referência de memória** em Python?

Em Python, **variáveis não armazenam diretamente os valores**, mas sim **referências (ponteiros) para os objetos na memória**.

Isso significa que:

* Se duas variáveis apontam para o **mesmo objeto**, uma alteração em uma **afeta a outra**.
* Isso acontece com **tipos mutáveis**, como **listas**, **dicionários**, **objetos personalizados**, etc.

---

### 📌 Exemplo simples:

```python
a = [1, 2, 3]
b = a  # b aponta para o mesmo objeto de a

b[0] = 99

print(a)  # [99, 2, 3]
print(b)  # [99, 2, 3]
```

➡ Aqui, `a` e `b` apontam para o **mesmo local na memória**.

---

## 🔍 Como ver o endereço de memória?

Use a função `id()` para verificar o identificador único (endereçamento interno):

```python
print(id(a))
print(id(b))  # mesmo valor
```

---

## ✅ Como copiar sem compartilhar referência?

Use **cópia explícita**, por exemplo:

### 1. **Fatiamento (slice)**:

```python
a = [1, 2, 3]
b = a[:]  # nova cópia
```

### 2. **Função `copy()`**:

```python
import copy
a = [1, 2, 3]
b = copy.copy(a)
```

### 3. **Para listas aninhadas (matrizes), use `deepcopy()`**:

```python
import copy
matriz = [[1, 2], [3, 4]]
nova_matriz = copy.deepcopy(matriz)
```

---

## 🧩 Exercício Prático – Mutabilidade e Referência

### 📋 Enunciado:

Crie uma lista chamada `original` com 5 números. Em seguida:

1. Atribua essa lista a uma nova variável `referencia`.
2. Modifique o primeiro elemento de `referencia`.
3. Mostre ambas as listas.
4. Mostre os `id()` de ambas para verificar se apontam para o mesmo endereço.
5. Agora, faça uma **cópia real** da lista original e mostre que modificar uma **não afeta** a outra.

---

### ✅ Código:

```python
import copy

original = [10, 20, 30, 40, 50]
referencia = original  # mesma referência

referencia[0] = 999

print("original:", original)
print("referencia:", referencia)
print("id(original):", id(original))
print("id(referencia):", id(referencia))

# Cópia real
copia = original[:]
copia[1] = 888

print("\nApós cópia:")
print("original:", original)
print("copia:", copia)
print("id(copia):", id(copia))
```

---

## 💡 Resumo Rápido:

| Conceito          | Significado                                                  |
| ----------------- | ------------------------------------------------------------ |
| `id()`            | Mostra o endereço de memória (identificador do objeto)       |
| Atribuição direta | Variáveis apontam para o mesmo objeto                        |
| `a[:]`, `copy()`  | Criam cópias **independentes** de objetos mutáveis           |
| `deepcopy()`      | Útil para **listas dentro de listas** (estruturas aninhadas) |

---

## 🧠 **O que são dicionários?**

Um **dicionário** (`dict`) é uma estrutura de dados que armazena pares **chave-valor**. Ele é **mutável**, **não ordenado** (até o Python 3.6) e **ideal para representar dados estruturados** como registros de pessoas, produtos, etc.

```python
pessoa = {
    "nome": "Ana",
    "idade": 30,
    "profissao": "Desenvolvedora"
}
```

Você acessa ou modifica os valores usando a chave:

```python
print(pessoa["nome"])           # Ana
pessoa["idade"] = 31            # Altera a idade
pessoa["linguagens"] = ["Python", "JS"]  # Adiciona nova chave
```

---

## ✅ **Exercício prático com dicionários**

### 🔍 Enunciado:

Crie um programa que gerencia um pequeno **cadastro de produtos** para um mercado.
Cada produto terá:

* Nome do produto
* Preço
* Quantidade em estoque

### Requisitos:

1. Cadastre 3 produtos usando dicionários.
2. Armazene todos os produtos em uma **lista**.
3. Calcule e exiba:

   * O produto mais caro.
   * O valor total do estoque (preço × quantidade de cada item, somando tudo).
   * O nome e valor total de cada produto.

---

### 💻 Exemplo de Código:

```python
produtos = []

for i in range(3):
    print(f"\nCadastro do produto {i+1}")
    nome = input("Nome do produto: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade em estoque: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)

# Produto mais caro
mais_caro = max(produtos, key=lambda p: p["preco"])
print(f"\n🤑 Produto mais caro: {mais_caro['nome']} - R$ {mais_caro['preco']:.2f}")

# Total do estoque
valor_total = 0
print("\n📦 Produtos e valor total individual:")
for p in produtos:
    total_individual = p["preco"] * p["quantidade"]
    valor_total += total_individual
    print(f"- {p['nome']}: R$ {p['preco']} × {p['quantidade']} = R$ {total_individual:.2f}")

print(f"\n💰 Valor total de todos os produtos no estoque: R$ {valor_total:.2f}")
```

---

### 💡 O que você pratica aqui:

* Uso e estrutura de **dicionários**.
* **Laços `for`** com dicionários em uma lista.
* Acesso, modificação e leitura de **valores por chave**.
* Cálculos com os dados armazenados.
* Funções `max()` com `lambda`.

---

## 🧠 O que são Conjuntos?

Conjuntos em Python (`set`) são coleções **não ordenadas**, **imutáveis no conteúdo (mas mutáveis na estrutura)** e **sem elementos duplicados**.

```python
linguagens = {"Python", "Java", "C++", "Python"}
print(linguagens)  # {'Java', 'Python', 'C++'} — sem duplicatas!
```

---

## ✅ Exercício com Conjuntos

### 🎯 Enunciado:

Você está desenvolvendo um sistema para um **grupo de estudos** com duas turmas: **Turma A** e **Turma B**.

1. Peça ao usuário os **nomes dos alunos** da Turma A e da Turma B (sem repetições).
2. Armazene os nomes em dois **conjuntos**.
3. Exiba:

   * ✅ Alunos que participam das **duas turmas**.
   * 🔄 Alunos que estão em **apenas uma turma**.
   * 📋 Todos os alunos únicos dos dois grupos.
   * ❌ Alunos que estão **somente na Turma A**.

---

### 💻 Exemplo de Código:

```python
# Entrada de dados
print("Digite os nomes dos alunos da Turma A (separados por vírgula):")
turma_a = set(input().split(","))
turma_a = {nome.strip() for nome in turma_a}

print("\nDigite os nomes dos alunos da Turma B (separados por vírgula):")
turma_b = set(input().split(","))
turma_b = {nome.strip() for nome in turma_b}

# Operações com conjuntos
intersecao = turma_a & turma_b
diferenca_simetrica = turma_a ^ turma_b
uniao = turma_a | turma_b
somente_a = turma_a - turma_b

# Resultados
print("\n✅ Alunos nas duas turmas:", intersecao)
print("🔄 Alunos em apenas uma das turmas:", diferenca_simetrica)
print("📋 Todos os alunos únicos:", uniao)
print("❌ Alunos só da Turma A:", somente_a)
```

---

### 🧠 O que você aprende:

* Criar e manipular **sets**.
* Eliminar **valores duplicados** automaticamente.
* Aplicar operações matemáticas de **interseção (`&`)**, **união (`|`)**, **diferença (`-`)** e **diferença simétrica (`^`)**.
* Boas práticas com `set comprehension`.

---

## 🧠 O que são funções?

Funções são blocos de código nomeados que executam uma tarefa específica.
São definidas com `def` e podem **receber parâmetros** e **retornar valores**.

```python
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Ana"))  # Olá, Ana!
```

---

## ✅ Exercício prático com funções

### 🎯 Enunciado:

Crie um sistema de cadastro de alunos usando funções.

1. Crie uma função `cadastrar_aluno` que recebe **nome, idade e curso** e retorna um **dicionário** com esses dados.
2. Crie uma função `exibir_alunos` que recebe uma **lista de alunos** e imprime todos de forma formatada.
3. Permita o cadastro de **vários alunos** usando um laço.
4. Ao final, exiba a lista completa dos alunos cadastrados.

---

### 💻 Código Exemplo:

```python
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

# Exibe todos os alunos
exibir_alunos(alunos)
```

---

### 🧠 O que você pratica aqui:

* Definir e chamar **funções com parâmetros**.
* Trabalhar com **retorno de função**.
* Armazenar dados em **listas e dicionários**.
* Uso de **laço `while`** para repetir o cadastro.
* Separação de responsabilidades e **organização do código**.

---

## 🧠 O que é Modularização?

**Modularização** é o processo de **dividir o código em módulos** (arquivos `.py`) para:

* Organizar melhor o projeto;
* Reutilizar código;
* Facilitar manutenção e testes;
* Tornar o sistema mais legível e escalável.

Em Python, usamos arquivos diferentes e importamos funções, classes ou variáveis entre eles.

---

## 📁 Estrutura de exemplo

```plaintext
meu_projeto/
├── main.py
├── cadastro.py
└── util.py
```

---

## 💡 Vamos construir isso com um exercício prático:

### 🎯 Enunciado:

Construa um sistema de cadastro de usuários com **modularização**.
Crie os seguintes arquivos:

1. **`cadastro.py`** — Contém funções relacionadas ao cadastro.
2. **`util.py`** — Contém funções auxiliares (ex: validação).
3. **`main.py`** — Onde o sistema roda, com menu interativo.

---

### 📄 cadastro.py

```python
def cadastrar_usuario(nome, idade):
    return {"nome": nome, "idade": idade}

def listar_usuarios(lista):
    print("\n👥 Usuários Cadastrados:")
    for u in lista:
        print(f"- {u['nome']} ({u['idade']} anos)")
```

---

### 📄 util.py

```python
def validar_idade(valor):
    try:
        idade = int(valor)
        if idade > 0:
            return idade
        else:
            print("Idade deve ser positiva.")
            return None
    except ValueError:
        print("Idade inválida. Digite um número.")
        return None
```

---

### 📄 main.py

```python
from cadastro import cadastrar_usuario, listar_usuarios
from util import validar_idade

usuarios = []

while True:
    print("\n=== Menu ===")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Nome: ")
        idade = None
        while idade is None:
            idade = validar_idade(input("Idade: "))
        usuarios.append(cadastrar_usuario(nome, idade))
    elif opcao == '2':
        listar_usuarios(usuarios)
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
```

---

## 🧠 O que você aprende com isso:

* Separar responsabilidades por arquivo (modularização).
* Usar `import` para organizar o sistema.
* Criar e reutilizar funções.
* Boa prática de manter o `main.py` como ponto de entrada.
* Validar dados de entrada de forma limpa e reutilizável.
* Rode com arquivo 'main.py'

---

## 🧠 O que é Tratamento de Exceções?

Erros acontecem. Em vez de deixar o programa quebrar com mensagens como `ValueError`, `ZeroDivisionError`, etc., usamos **blocos try/except** para capturar e lidar com esses erros de forma controlada.

---

## 🧪 Exemplo simples

```python
try:
    numero = int(input("Digite um número: "))
    print("Número ao quadrado:", numero ** 2)
except ValueError:
    print("⚠️ Você não digitou um número inteiro válido.")
```

---

## 🔄 Estrutura Geral

```python
try:
    # código que pode dar erro
except TipoDoErro:
    # tratamento do erro
else:
    # executa se NÃO houver erro
finally:
    # sempre executa (com ou sem erro)
```

---

## 💡 Tipos comuns de exceções

* `ValueError` – Conversão inválida (ex: `int("abc")`)
* `ZeroDivisionError` – Divisão por zero
* `FileNotFoundError` – Arquivo não encontrado
* `IndexError` – Índice inválido em listas
* `KeyError` – Chave inexistente em dicionários
* `TypeError` – Operação inválida entre tipos

---

## 📝 Exercício Prático – Calculadora com tratamento de erros

### 🎯 Enunciado:

Crie uma calculadora que:

* Solicite dois números ao usuário
* Solicite a operação (+, -, \*, /)
* Exiba o resultado
* Trate possíveis erros, como:

  * Entrada inválida
  * Divisão por zero
  * Operação inválida

---

### ✅ Código:

```python
def calcular(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    else:
        raise ValueError("Operação inválida!")

try:
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ")

    resultado = calcular(a, b, operacao)
    print("✅ Resultado:", resultado)

except ZeroDivisionError:
    print("❌ Erro: divisão por zero não é permitida.")
except ValueError as ve:
    print(f"❌ Erro de valor: {ve}")
except Exception as erro:
    print("❌ Ocorreu um erro inesperado:", erro)
finally:
    print("🧾 Fim do programa.")
```

---

## 🧪 O que você aprendeu aqui:

* Como usar `try/except/else/finally`
* Como capturar **erros específicos**
* Como deixar sua aplicação mais amigável ao usuário
* Como evitar que o programa trave por causa de entradas erradas

---

## 🚨 `raise`: lançando erros manualmente

### 🧠 O que é?

Você usa `raise` quando quer **forçar uma exceção** se algo não está certo no seu código.

### 📌 Exemplo:

```python
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero!")
    return a / b

print(dividir(10, 2))  # ✅
print(dividir(10, 0))  # ❌ Vai lançar uma exceção
```

---

## ✅ Quando usar `raise`?

* Para **validar dados recebidos**
* Para **parar a execução** se uma regra de negócio for violada
* Em conjunto com `try/except` para **repropagar** erros

---

## 🧪 Exemplo real com `raise`

```python
def cadastrar_usuario(nome, idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa!")
    return {"nome": nome, "idade": idade}

try:
    user = cadastrar_usuario("Ana", -5)
except ValueError as e:
    print("Erro:", e)
```

---

## 🧪 `assert`: verificações em tempo de desenvolvimento

### 🧠 O que é?

`assert` é usado para **verificar condições que *devem* ser verdadeiras** durante o desenvolvimento. Se a condição for falsa, lança um `AssertionError`.

### 📌 Exemplo:

```python
def calcular_media(valores):
    assert len(valores) > 0, "A lista de valores não pode estar vazia."
    return sum(valores) / len(valores)

print(calcular_media([10, 8, 9]))  # ✅
print(calcular_media([]))         # ❌ AssertionError
```

---

## ✅ Quando usar `assert`?

* Durante testes e debugging
* Para validar pré-condições (ex: listas não vazias)
* Em funções que só devem aceitar valores válidos

> ⚠️ Atenção: `assert` pode ser **ignorado** se o Python for executado com a flag `-O` (modo otimizado). Use com sabedoria!

---

## 📘 Comparativo Rápido

| Comando  | Para que serve?                           | Exceção lançada  |
| -------- | ----------------------------------------- | ---------------- |
| `raise`  | Lançar exceções personalizadas            | Qualquer exceção |
| `assert` | Garantir que algo seja verdadeiro (debug) | `AssertionError` |

---

## 🧪 Exercício proposto

**Enunciado:**

Crie uma função chamada `transferir_saldo` que recebe:

* `saldo_atual`
* `valor_transferencia`

A função deve:

* Lançar um `ValueError` se o valor for maior que o saldo
* Usar `assert` para garantir que o valor seja positivo
* Retornar o novo saldo após a transferência

**Exemplo de uso:**

```python
try:
    novo_saldo = transferir_saldo(1000, 300)
    print("Transferência concluída. Novo saldo:", novo_saldo)
except Exception as e:
    print("Erro:", e)
```

---

## 🌀 **Geradores em Python** — explicação e exercício

### 📘 **O que são geradores?**

Geradores são uma forma especial de criar **iteradores em Python**, que **geram valores sob demanda** usando a palavra-chave `yield`.
Diferente de listas, **não armazenam todos os valores na memória** — eles produzem um valor por vez, de forma eficiente.

---

### 🚀 **Vantagens:**

* Usam **menos memória**
* Podem gerar sequências **infinitas**
* Muito úteis em **laços**, **streams**, ou **cálculos demorados**

---

### 🧪 Exemplo simples:

```python
def contador():
    for i in range(3):
        yield i

for num in contador():
    print(num)
```

📤 Saída:

```
0
1
2
```

---

## ✅ **Exercício – Gerador de Números Pares dentro de um intervalo**

**Enunciado:**
Crie um gerador chamado `gerador_pares(inicio, fim)` que receba dois números e gere **todos os números pares** entre `inicio` e `fim` (inclusive).
Depois, utilize um `for` para imprimir todos os valores gerados.

---

### 💡 Dica:

Use `yield` para retornar os pares um a um, sem armazená-los em uma lista.

---

### 🧩 Código base:

```python
def gerador_pares(inicio, fim):
    for num in range(inicio, fim + 1):
        if num % 2 == 0:
            yield num

# Teste
inicio = 3
fim = 15

print("Pares entre", inicio, "e", fim, ":")
for par in gerador_pares(inicio, fim):
    print(par)
```

### ✅ **Como instalar o `asizeof` corretamente**

`asizeof` é uma função do pacote **[`pympler`](https://pypi.org/project/Pympler/)**, que serve para medir o **tamanho real de objetos na memória** em Python.

#### 👉 Passo 1: Instalar o pacote

No terminal ou prompt de comando:

```bash
pip install pympler
```

---

#### 👉 Passo 2: Usar o `asizeof`

```python
from pympler import asizeof

lista = [1, 2, 3, 4, 5]
print("Tamanho da lista em bytes:", asizeof.asizeof(lista))
```

---

### 🧠 O que ele faz?

Diferente de `sys.getsizeof()`, o `asizeof()` calcula **todo o tamanho recursivo do objeto**, considerando subestruturas (como listas dentro de listas, objetos compostos etc).

---

## ⚡ O que é uma função `lambda`?

Uma função `lambda` é uma forma **concisa de criar funções anônimas** (sem `def`, sem nome) em **uma linha só**.

### 📌 Sintaxe:

```python
lambda argumentos: expressão
```

### 🔍 Exemplo:

```python
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10
```

---

## ✅ Exercício 1 – Ordenar uma lista de tuplas com `lambda`

### 📘 Enunciado:

Dada uma lista de pessoas com nome e idade, use a função `sorted()` com uma função `lambda` para **ordenar por idade**.

### 🧩 Código base:

```python
pessoas = [
    ("Alice", 30),
    ("Bob", 25),
    ("Carol", 35),
    ("Dan", 22)
]

# Ordenar pela idade
ordenadas = sorted(pessoas, key=lambda pessoa: pessoa[1])

print("Pessoas ordenadas por idade:")
for nome, idade in ordenadas:
    print(f"{nome} - {idade} anos")
```

---

## ✅ Exercício 2 – Filtrar números pares com `lambda` + `filter`

### 📘 Enunciado:

Use `lambda` com a função `filter()` para obter **apenas os números pares** de uma lista.

```python
numeros = list(range(1, 21))

pares = list(filter(lambda x: x % 2 == 0, numeros))

print("Números pares:", pares)
```

---

## ✅ Exercício 3 – Dobrar todos os valores com `lambda` + `map`

```python
numeros = [1, 2, 3, 4, 5]

dobrados = list(map(lambda x: x * 2, numeros))

print("Valores dobrados:", dobrados)
```

---

### 💡 Dica bônus:

Você pode usar `lambda` com `sorted()`, `map()`, `filter()` e até dentro de dicionários ou listas.

---

## 🧪 O que é `filter()`?

A função **`filter(func, iterable)`** retorna apenas os elementos do iterável para os quais a função retorna `True`.

### 📌 Sintaxe:

```python
filter(função, iterável)
```

> A função geralmente é uma `lambda`, mas pode ser uma função nomeada também.

---

## ✅ Exemplo simples com `lambda`

```python
numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))

print(pares)  # Saída: [2, 4, 6]
```

---

## 💡 Exemplo com função nomeada

```python
def eh_maior_que_10(n):
    return n > 10

lista = [5, 12, 8, 20, 3, 15]
maiores = list(filter(eh_maior_que_10, lista))

print(maiores)  # Saída: [12, 20, 15]
```

---

## ✅ Exercício proposto

### 🎯 **Exercício – Filtrar nomes com mais de 5 letras**

#### Enunciado:

Dada uma lista de nomes, filtre apenas os que têm mais de 5 letras usando `filter()`.

```python
nomes = ["Ana", "Beatriz", "Carlos", "Eva", "Fábio", "Gabriela"]

nomes_filtrados = list(filter(lambda nome: len(nome) > 5, nomes))

print("Nomes com mais de 5 letras:", nomes_filtrados)
```

---

## 🔍 Outro exercício

### 🎯 **Filtrar números positivos e ímpares**

```python
numeros = [-5, -2, 0, 1, 3, 4, 7, 10, -1]

positivos_impares = list(filter(lambda x: x > 0 and x % 2 != 0, numeros))

print("Positivos e ímpares:", positivos_impares)
```

---

## 🧠 O que é `map()`?

A função **`map()`** aplica uma função a **cada item de um iterável** (como lista ou tupla) e retorna um iterador com os resultados.

### 📌 Sintaxe:

```python
map(função, iterável)
```

Geralmente usamos com `lambda`, mas pode ser qualquer função.

---

## ✅ Exemplo simples:

```python
numeros = [1, 2, 3, 4, 5]
dobrados = list(map(lambda x: x * 2, numeros))
print(dobrados)  # Saída: [2, 4, 6, 8, 10]
```

---

## ✅ Exemplo com função nomeada:

```python
def quadrado(x):
    return x ** 2

valores = [1, 2, 3, 4]
resultado = list(map(quadrado, valores))
print(resultado)  # Saída: [1, 4, 9, 16]
```

---

## ✅ Exemplo com várias listas:

```python
a = [1, 2, 3]
b = [4, 5, 6]

somas = list(map(lambda x, y: x + y, a, b))
print(somas)  # Saída: [5, 7, 9]
```

---

## 🧪 Exercícios com `map()`

### 🎯 **Exercício 1 – Converter para maiúsculas**

**Enunciado:**
Dada uma lista de nomes, crie uma nova lista com todos os nomes em letras maiúsculas usando `map()`.

```python
nomes = ["ana", "bruno", "carla", "daniel"]
maiusculos = list(map(lambda nome: nome.upper(), nomes))
print(maiusculos)  # ['ANA', 'BRUNO', 'CARLA', 'DANIEL']
```

---

### 🎯 **Exercício 2 – Calcular o dobro dos salários**

**Enunciado:**
Você tem uma lista com os salários de alguns funcionários. A empresa vai dobrar os salários. Use `map()` para gerar a nova lista.

```python
salarios = [1200, 2500, 1850, 4000]
dobrados = list(map(lambda s: s * 2, salarios))
print(dobrados)  # [2400, 5000, 3700, 8000]
```

---

### 🎯 **Exercício 3 – Converter temperaturas**

**Enunciado:**
Dada uma lista de temperaturas em Celsius, converta todas para Fahrenheit usando a fórmula:

```
F = C * 1.8 + 32
```

```python
celsius = [0, 20, 30, 37, 100]
fahrenheit = list(map(lambda c: c * 1.8 + 32, celsius))
print(fahrenheit)  # [32.0, 68.0, 86.0, 98.6, 212.0]
```

---

## 📂 Trabalhando com Arquivos em Python

### ✅ Abrir arquivos

```python
arquivo = open('exemplo.txt', 'r')  # r = read (leitura)
conteudo = arquivo.read()
arquivo.close()
```

### ✅ Escrever em arquivos

```python
arquivo = open('exemplo.txt', 'w')  # w = write (reescreve)
arquivo.write('Olá, mundo!')
arquivo.close()
```

### ✅ Acrescentar dados (sem apagar o que já existe)

```python
arquivo = open('exemplo.txt', 'a')  # a = append
arquivo.write('\nNova linha')
arquivo.close()
```

### ✅ Leitura linha por linha

```python
with open('exemplo.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

> `with` cuida do fechamento automático do arquivo – mais seguro e recomendado.

---

## 🧪 Exercício com Arquivos

### 📌 **Exercício – Cadastro de nomes em arquivo**

### 🧩 Enunciado:

Crie um programa que:

1. Pergunte ao usuário quantos nomes deseja cadastrar.
2. Peça os nomes um por um.
3. Salve esses nomes no arquivo `nomes.txt`, um por linha.
4. Em seguida, leia o arquivo e exiba todos os nomes cadastrados.

---

### 💡 Dica:

* Use `open()` com `'w'` para escrever.
* Use `with open(...)` para leitura.
* Use `input()` para receber os nomes.

---

### ✅ Exemplo de solução:

```python
qtd = int(input("Quantos nomes deseja cadastrar? "))

with open('nomes.txt', 'w') as arquivo:
    for i in range(qtd):
        nome = input(f"Digite o {i + 1}º nome: ")
        arquivo.write(nome + '\n')

print("\nNomes cadastrados:")
with open('nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha.strip())
```

---

Aqui estão os principais **modos de abertura de arquivos**:

## 📖 Modos de abertura de arquivos no Python

| Modo   | Significado              | Comportamento                                                                            |
| ------ | ------------------------ | ---------------------------------------------------------------------------------------- |
| `'r'`  | **Read (leitura)**       | Abre um arquivo existente para leitura. Erro se o arquivo não existir.                   |
| `'w'`  | **Write (escrita)**      | Cria um novo arquivo ou **apaga todo o conteúdo** se já existir.                         |
| `'a'`  | **Append (acrescentar)** | Abre para escrita **no final do arquivo**, sem apagar o conteúdo existente.              |
| `'x'`  | **Create (exclusiva)**   | Cria um novo arquivo, mas **gera erro se ele já existir**.                               |
| `'r+'` | **Read + Write**         | Abre o arquivo para **leitura e escrita**. Erro se não existir.                          |
| `'w+'` | **Write + Read**         | Cria ou apaga o arquivo existente para **escrita e leitura**.                            |
| `'a+'` | **Append + Read**        | Abre para **leitura e escrita**, escrevendo **no final**. Cria o arquivo se não existir. |

---

## 📌 Exemplos:

### Leitura:

```python
with open('arquivo.txt', 'r') as f:
    print(f.read())
```

### Escrita:

```python
with open('arquivo.txt', 'w') as f:
    f.write("Olá!")
```

### Acrescentar:

```python
with open('arquivo.txt', 'a') as f:
    f.write("\nNova linha")
```

### Leitura + Escrita:

```python
with open('arquivo.txt', 'r+') as f:
    conteudo = f.read()
    f.write("\nMais dados")
```

---

## 🥒 O que é `pickle`?

O módulo `pickle` serve para:

* **Serializar** objetos Python → transformar em bytes e salvar em arquivos.
* **Desserializar** arquivos → recuperar os objetos Python do jeito que estavam.

---

## 📦 Quando usar?

Use `pickle` quando quiser salvar:

* Listas, dicionários, conjuntos
* Objetos de classes personalizadas
* Qualquer estrutura de dados em Python que você queira reutilizar depois

---

## ✅ Como usar o `pickle`?

### 1. Salvando (serializando) um objeto:

```python
import pickle

dados = {"nome": "Ana", "idade": 30, "notas": [9.0, 8.5, 10]}

with open('dados.pkl', 'wb') as arquivo:
    pickle.dump(dados, arquivo)
```

> Use `'wb'` = write binary (escrever em binário)

---

### 2. Lendo (desserializando) o objeto:

```python
import pickle

with open('dados.pkl', 'rb') as arquivo:
    dados_carregados = pickle.load(arquivo)

print(dados_carregados)
```

> Use `'rb'` = read binary (ler em binário)

---

## ⚠️ Atenção:

* Nunca use `pickle.load()` com arquivos desconhecidos ou inseguros — **pode rodar código malicioso**.
* Serve **apenas para Python** — não é compatível com outras linguagens (ao contrário do JSON, por exemplo).

---

## 🧠 Funções principais do `pickle`

| Função            | Uso principal                                              | Trabalha com... |
| ----------------- | ---------------------------------------------------------- | --------------- |
| `dump(obj, file)` | Serializa e salva um objeto em um arquivo                  | Arquivos (`wb`) |
| `load(file)`      | Carrega e desserializa um objeto de um arquivo             | Arquivos (`rb`) |
| `dumps(obj)`      | Serializa um objeto e retorna bytes (em memória)           | Variáveis       |
| `loads(bytes)`    | Desserializa de uma string de bytes para o objeto original | Variáveis       |

---

## ✅ Exemplo prático com `dump` e `load` (arquivo)

```python
import pickle

dados = {"nome": "Ana", "idade": 30}

# Salvando em arquivo
with open('dados.pkl', 'wb') as f:
    pickle.dump(dados, f)

# Lendo do arquivo
with open('dados.pkl', 'rb') as f:
    recuperado = pickle.load(f)

print(recuperado)
```

---

## ✅ Exemplo prático com `dumps` e `loads` (em memória)

```python
import pickle

dados = {"nome": "João", "idade": 25}

# Serializando em memória (bytes)
bytes_serializados = pickle.dumps(dados)
print("Bytes serializados:", bytes_serializados)

# Desserializando da memória
recuperado = pickle.loads(bytes_serializados)
print("Objeto original:", recuperado)
```

---

## 🧪 Comparação

```python
# Com arquivos
pickle.dump(objeto, arquivo)   ↔   objeto = pickle.load(arquivo)

# Em memória (strings de bytes)
pickle.dumps(objeto)           ↔   objeto = pickle.loads(bytes)
```

---

## 🧩 Dica de uso

Use `dumps`/`loads` quando quiser:

* Enviar objetos Python em **APIs, sockets, redes** ou
* Armazenar objetos em **banco de dados binário ou memória temporária**.

Use `dump`/`load` quando quiser:

* Trabalhar com **arquivos físicos .pkl**

---




