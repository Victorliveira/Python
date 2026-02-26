# Programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas.

from random import randint

print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR:')
print('=-'*20)
n = npc = cont = s =0
esc = resultado = 's'

while True:
    npc = randint(0,10)
    n = int(input('Diga um valor: '))
    esc = input('Par ou Ímpar? [P/I] ').upper()
    while esc not in ('PI'):
        print('Escolha invalida, selecione novamente!')
        esc = input('Par ou Ímpar? [P/I] ').upper()
    s = npc + n
    resultado = 'PAR' if s%2 ==0 else 'ÍMPAR'
    print(f'Você jogou {n} e o computador {npc}. Total de {s} DEU {resultado}')
    if esc == 'P' and s % 2 == 0:
        print('Você VENCEU!')
        cont+=1
        print('Vamos jogar novamente...')
    elif esc == 'I' and s % 2 != 0:
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        cont+=1
    else:
        print('Você PERDEU!')
        break
print(f'GAME OVER. Você venceu {cont} vezes.')