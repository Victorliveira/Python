#programa que faça o computador jogar Jokenpô com vc

import random
import time
print('='*30)
print('INICIANDO JOKENPÔ')
print('='*30)
time.sleep(1.5)

comp = ['pedra','papel','tesoura'] #Escolha do computador
esc_comp = random.choice(comp)
print('O Computador escolheu entre pedra, papel ou tesoura.')
time.sleep(0.5)
print('Qual você vai escolher?')
esc = input('')

if esc == 'pedra' and esc_comp == 'tesoura' or esc == 'papel' and esc_comp == 'pedra' or esc == 'tesoura' and esc_comp == 'papel':
    print(f'Parabéns! Você venceu.\nO computador escolheu {esc_comp}')
elif esc == 'tesoura' and esc_comp == 'pedra' or esc == 'pedra' and esc_comp == 'papel' or esc == 'papel' and esc_comp == 'tesoura':
    print(f'Você perdeu!\nO computador escolheu {esc_comp}')
elif esc == 'tesoura' and esc_comp == 'tesoura' or esc == 'pedra' and esc_comp == 'pedra' or esc == 'papel' and esc_comp == 'papel':
    print('EMPATE')

