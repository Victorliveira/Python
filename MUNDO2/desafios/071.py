#Programa que simule o funcionamento de um caixa eletrônico, No início, pergunte ao usuários qual será o valor sacado(int), o programa vai informar quantas cédulas de cada valor serão entregues. Considere que o caixa possui cédulas de 50,20,10 e 1
print('='*30)
print('BANCO VICTOR'.center(30))
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))

sobra50 = sobra20 = sobra10 = sobra1 = 0

while valor !=0:
    sobra50 = valor // 50
    valor %= 50
    sobra20 = valor // 20
    valor %= 20
    sobra10 = valor // 10
    valor %= 10
    sobra1 = valor // 1
    valor %= 1

if sobra50 !=0:
    print(f'Total de {sobra50} cédulas de R$50')
if sobra20 !=0:
    print(f'Total de {sobra20} cédulas de R$20')
if sobra10 !=0:
    print(f'Total de {sobra10} cédulas de R$10')
if sobra1 !=0:
    print(f'Total de {sobra1} cédulas de R$1')
print('='*30)
print('Volte sempre ao BANCO VICTOR! Tenha um bom dia!')