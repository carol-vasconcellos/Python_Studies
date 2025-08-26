nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

def retorna_nome(nomes, alvo):
    for i in range(len(nomes)):
        if nomes[i] == alvo:
            return i
    return None

print(retorna_nome(nomes, "Carlos"))  # Saída: 2    
print(retorna_nome(nomes, "Mariana"))   # Saída: None