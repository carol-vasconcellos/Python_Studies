''' Peça ao usuário a distância percorrida (km) e o combustível gasto (litros). Calcule o consumo médio. '''

distancia_percorrida = float(input("A distancia percorrida: "))
combustivel_gasto = float(input("Combustivel gasto: "))

consumo_medio = distancia_percorrida / combustivel_gasto

print(f"O consumo médio é: {consumo_medio}, km/l")
