#Programa que leia um num int e diga se ele é ou não um num primo.

pr = int(input('\33[mInforme um número: '))
tot = 0
for c in range(1,pr+1):
    if pr %c ==0:
        print(f'\033[32m{c}', end=' ')
        tot += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\n\33[mO número {pr} foi divísivel {tot} vezes')
if tot == 2:
    print('E por isso ele É PRIMO')
else:
    print('E por isso ele NÃO É PRIMO')




if pr == 2 or pr == 3:
    print(f'O número {pr} é um número primo')
elif pr%2 !=0 and pr%3 !=0:
    print(f'O número {pr} é um número primo')
else:
    print(f'O número {pr} não é um número primo')




