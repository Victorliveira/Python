#interactive help é uma função do python que ajuda com qlq função

'''help()
help(print)'''

def contador(i,f,p):
    """
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    
    c = i
    while c<= f:
        print(f'{c}', end=' ')
        c +=p
    print('FIM!')

contador(2,10,2)
help(contador)

#criando um parâmetro opcional.
'''def somar(a,b,c=0):
    s = a+b+c
    print(f'A soma vale {s}')'''

#somar(3,2,5)
#somar(8,4)

# escopo de variável

def teste(b):
    global a # Manda o Python usar a variável global invés de criar uma local
    a = 8 
    # escopo local
    b+= 4
    c=2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro valee {c}')

a = 5 # escopo global
teste(a)
print(f'A fora vale {a}')


# Retornando valores

def somar(a=0,b=0,c=0):
    s = a+b+c
    return s

print(somar(3,2,5))

r1 = somar(2,3)
r2 = somar(2,2)

print(f'Os resultados são {r1} e {r2}')

