# Programa que tenha uma função chamad área(), que receba as dimensões de um terro retangular(largura e comprimento) e mostre a área do terreno

def área(l,c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m².')

print('Controle de Terrenos')
print('-'*20)
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))

área(largura,comprimento)
