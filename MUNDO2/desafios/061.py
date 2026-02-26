# Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando while

print('='*30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('='*30)
prim = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão: '))
n = 1
while n <11:
    print(prim+(n-1)*(raz), end= ' -> ')
    n += 1
print('ACABOU')