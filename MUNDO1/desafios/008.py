# Programa que leia um valor em metros e exiba convertido em cm e mm

metro = float(input('Informe a metragem: '))
cm = metro * 100
mm = metro * 1000

print(f'Em {metro} metros, tem {cm} centímetros e {mm} milimetros')