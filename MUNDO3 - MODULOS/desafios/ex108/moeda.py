def metade(num=0):
    return num/2

def dobro(num=0):
    return num*2

def aumentar(num=0,p=0):
    num = num+(num*(p/100))
    return num

def diminuir(num=0,p=0):
    num = num-(num*(p/100))
    return num

def moeda(num=0,moeda = 'R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')