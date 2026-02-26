#Programa que leia um num qlq e mostre o seu fatorial. ex: 5! =5*4*3*2*1 = 120
# fazer com while e for
print('='*30)
print('CÁLCULO DO FATORIAL')
print('='*30)
fat = int(input('Informe um número: '))
num = fat
cont = fat

print(f'Calculando {num}! = ', end='')
while fat > 0:   
    print(f'{fat}', end='')
    print(' * ' if fat > 1 else ' = ', end='')
    if fat > 1:
        cont = cont * (fat -1)
        fat = fat -1
    elif fat == 1:
        fat = 0
print(cont)

