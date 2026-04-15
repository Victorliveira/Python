# Programa que tenha uma função chamad área(), que receba as dimensões de um terro retangular(largura e comprimento) e mostre a área do terreno

def área(l,m):
    a = l * m
    print(f'A área do seu terreno {l}x{m}, é de {a}m².')

print('Controle de Terrenos')
print('-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

área(largura,comprimento)
