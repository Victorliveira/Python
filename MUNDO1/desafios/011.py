#Programa que le a altura e largura de uma parede em metros, calcula a área e a quantidade de tina necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²

alt = float(input('Qual a altura a parede? '))
lar = float(input('Qual a largura da parede? '))

area = alt * lar
tinta = area / 2

print(f'É necessário {tinta} litros de tinta para pintar uma área de {area}m²')