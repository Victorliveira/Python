#programa que faça o computador jogar Jokenpô com vc

import random
import time
print('INICIANDO JOKENPÔ')
time.sleep(1.5)
print('O Computador escolheu entre pedra, papel ou tesoura.')
time.sleep(0.5)
print('Qual você vai escolher?')
esc = input('')

comp = random.random['pedra','papel','tesoura']
print(comp)