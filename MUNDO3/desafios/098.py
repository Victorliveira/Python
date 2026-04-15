# Programa que tenha uma função chamada contador(), que receba 3 parâmetros: ínicio, fim e passo e realize a contagem.
# O programa tem que realizar 3 contagens atravé da função criada: a) de 1 até 10, de 1 em 1. b) De 10 até 0, de 2 em 2. C) uma contagem personalizada

from time import sleep

def contador(i,f,p):
    if p == 0:
        p = 1
    if p <0:
        p = p *-1
    print(f'Contagem de {i} até {f} pulando de {p} em {p}')
    sleep(0.5)
    if i < f:
        while i <= f:
            sleep(0.2)
            print(i, end=' ')
            i+=p
    else:
        while i >= f:
            sleep(0.2)
            print(i, end=' ')
            i-=p     
    sleep(0.2)  
    print('FIM!')

contador(1,10,1)
contador(10,0,2)

print('Personalize a contagem!')
ini = int(input('Início: '))
fim = int(input('Final: '))
passo = int(input('Passo: '))

contador(ini,fim,passo)