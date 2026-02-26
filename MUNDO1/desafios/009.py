#Programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

num = float(input('Digite um número: '))
print('='*20)
i = 1
while i <11:
    print(f'{num} * {i} = {num * i}')
    i = i + 1
print('='*20)