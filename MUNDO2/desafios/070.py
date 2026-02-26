# Programa que leia o nome e o preço de vários produtos. O Programa deverá perguntar se o usuário vai continuar. No final, mostre:
#a - total gasto na compra b-Quantos produtos custam mais de R$1000 c- qual o nome do produto mais barato

valor = total = contp = valorb = 0
nome = nomep = 's'
print('-'*25)
print('LOJA SUPER BARATÃO')
print('-'*25)

while True:
    print('='*25)
    nome = input('Nome do produto: ').capitalize()
    valor = int(input('Valor: R$ '))
    print('='*25)
    if total == 0:
        valorb = valor
    if valorb > valor:
        nomep = nome
        valorb = valor
    if valor > 1000:
        contp+=1
    total+= valor
    seguir = input('Continuar? [S/N] ').upper()
    while seguir not in ('SN'):
        print('Operação INVÁLIDA, digite novamente')
        seguir = input('Continuar? [S/N] ').upper()
    if seguir == 'N':
        break
print('-----FIM DO PROGRAMA-----')
print(f'Foi gasto R${total:.2f} na compra!')
print(f'{contp} produtos custaram mais que R$1000.0')
print(f'O produto {nomep} foi o produto mais barato, custando R${valorb:.2f}')