# Prorgama que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta

from random import randint
from time import sleep

print('Gerador de bilhetes MEGA SENA!')
sleep(0.5)
qte = int(input('Deseja realizar quantos palpites? '))

cont = 1

print('Gerando palpites...')
print()
sleep(1)
for c in range(qte):
    ticket = []
    while len(ticket) <6:
        num = randint(1,60)
        if num not in ticket:
            ticket.append(num)
    sleep(0.6)
    print(f'jogo {cont}: ',ticket)
    cont+=1
print()
print('PROGRAMA FINALIZADO')