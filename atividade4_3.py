def calcular_area_quadrado(lado):
    area = lado ** 2
    area = calcular_area_quadrado(lado)
    return area
area = float(input('Digite o area do Quadrado: '))
dobro_area = area ** 2
print(f"A área do quadrado é {area}.")
print(f"O dobro da área do quadrado é {dobro_area}.")