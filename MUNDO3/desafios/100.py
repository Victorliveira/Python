# Programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A função sorteia() vai sortear 5 números e vai colocá-los dentro da lsita e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lst):
    print('Sorteando os 5 valores da lista:', end=' ')
    for c in range(0,5):
        sleep(0.3)
        lst.append(randint(0,10))
        print(lst[c], end=' ')
    print('PRONTO!')

def somaPar(lst):
    p = 0
    for c in lst:
        if c %2 == 0:
            p+=c
    print(f'Somando os valores pares de {lst}, temos {p}')

números = list()
sorteia(números)
somaPar(números)