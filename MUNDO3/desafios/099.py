# Programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. O Programa tem que analisar todos os valores e dizer qual dele é o maior.

from time import sleep

def maior(*lst):
    print('-='*30)
    print('Analisando os valores passados...')
    for c in lst:
        sleep(0.15)
        print(c, end=' ')
    print(f'Foram informados {len(lst)} valores ao todo')
    print(f'O maior valor informado foi', end=' ')
    if lst:
        print(max(lst))
    else:
        print('0')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()