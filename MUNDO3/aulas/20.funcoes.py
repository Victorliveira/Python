#funções servem para fazer algo repetitivo que n foi configurado pelo python

def mostralinha():
    print('-='*15)

def mensagem(msg):
    mostralinha()
    print(f'{msg:^30}')
    mostralinha()

mensagem('SISTEMA DE ALUNOS')
mensagem('PYTHON')

def som(a,b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')

som(4,5)
som(b=5,a=6)


def contador(*núm): #empacotamento
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')

contador(5,7,3,1,4)
contador(8,4,7)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos +=1
    print(lst)

valores = [7,2,5,0,4]

dobra(valores[:])
print(valores)