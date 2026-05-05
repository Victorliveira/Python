

def metade(num=0, f=False):
    if f:
         return moeda(num/2) 
    return num/2

def dobro(num=0, f=False):
    if f:
        return moeda(num*2)
    return num*2

def aumentar(num=0,p=0, f=False):
    num = num+(num*(p/100))
    if f:
        return moeda(num)
    return num

def diminuir(num=0,p=0, f=False):
    num = num-(num*(p/100))
    if f:
        return moeda(num)
    return num

def moeda(num=0,moeda ='R$'):
    return f'{moeda}{num:.2f}'.replace('.',',')