#Programa que leia o primeiro termo e a razão de uma PA, No final, mostre os 10 primeiros termos dessa progressão.
print('='*30)
print('10 PRIMEIROS TERMOS DE UMA PA')
print('='*30)
prim = int(input('Informe o primeiro termo: '))
raz = int(input('Informe a razão: '))
n = 1
for c in range(0,10):
    print(prim+(n-1)*(raz), end= ' -> ')
    n += 1
print('ACABOU')

    