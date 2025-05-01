# Python_Studies

## *Índice*

- [Introdução](#introdução)
- [Variáveis](#variáveis)
- [Tipos de dados](#tipos-de-dados)
- [Entrada e Saída de Dados](#entrada-e-saída-de-dados)
- [Conversão de Dados](#conversão-de-dados)
- [Operadores Aritméticos](#operadores-aritméticos)

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

### 🔹 Principais operadores:

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




