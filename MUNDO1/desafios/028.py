#Programa que faça o computador pensar em um número int entre 0 e 5 e peça para o usuário tentar descobrir qual foi o num escolhido.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint

num = randint(0,5)

print('-=-' * 10)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 10)

esc = int(input('Selecione um número de 0 a 5: '))
print(f'O computador escolheu o número: {num}')
if num == esc:
    print('Parabéns, vc acertou o número!')
else:
    print('Você não acertou o número')