# inverter uma string

def inverter_string(texto):
     return texto[::-1]

print(inverter_string("Python"))

# contar vogais

def contar_vogais(texto):
     vogais = 'AEIOUaeiou'
     contador_vogais = 0

     for letra in texto:
          if letra in vogais:
               contador_vogais += 1
     return contador_vogais

print(contar_vogais("Python"))