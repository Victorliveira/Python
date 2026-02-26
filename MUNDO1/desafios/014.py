# programa que le a temperatura C° e converte para farenheit

grau = float(input('Informe a temperaturaem °C: '))

faren = grau * 1.8 + 32
kevin = grau + 273.15

print(f'A temperatura de {grau}°C corresponde a {faren:.2f}°F e {kevin:.2f}°K!')