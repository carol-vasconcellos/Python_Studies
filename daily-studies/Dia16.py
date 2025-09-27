def pares_decrescente(lista):
    # Passo 1: Filtrar apenas os números pares
    # Um número é par se o resto da divisão por 2 é zero (num % 2 == 0)
    numeros_pares = []
    for num in lista:
        if num % 2 == 0:
            numeros_pares.append(num)
            
    # Passo 2: Ordenar a lista de pares em ordem decrescente
    # Usamos o método .sort() com o argumento 'reverse=True'
    numeros_pares.sort(reverse=True)
    
    # Passo 3: Retornar o resultado
    return numeros_pares

# Exemplo de Teste
lista_original = [5, 2, 9, 8, 10, 3] 
resultado = pares_decrescente(lista_original)

print(f"Resultado (Pares Decrescentes): {resultado}")


# Trocar vogais

# Seu código:
def trocar_vogais(texto):
    texto_modificado = texto
    vogais = "aeiouAEIOU"
    
    for vogal in vogais:
        texto_modificado = texto_modificado.replace(vogal, "*")
    
    return texto_modificado

print(trocar_vogais("python é divertido"))