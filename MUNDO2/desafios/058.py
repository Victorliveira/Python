# Melhore o jogo do DESAFIO28 onde o computador vai 'pensar' em um num entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer

from random import randint
import time
print('='*30)
print('O computador pensou em um número entre 0 a 10')
print('='*30)
time.sleep(0.5)

comp = randint(0,10) # número que o computador pensou
tot = 0 #contador dos chutes incorretos
esc = -1

while esc != comp:
    time.sleep(0.5)
    esc = int(input('\nAdivinhe o número!'))
    tot += 1
    if esc < comp:
        print('Eu pensei em um número maior..')
    elif esc > comp:
        print('Eu pensei em um número menor..')
    if esc != comp:
        print('Não foi esse número que pensei. Tente novamente!')
print(f'Parabéns você acertou em {tot} tentativas')