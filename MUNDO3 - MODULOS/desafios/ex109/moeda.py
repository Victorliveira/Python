

def metade(num, f=False):
    if f:
         return moeda(num/2) 
    return num/2

def dobro(num, f=False):
    if f:
        return moeda(num*2)
    return num*2

def aumentar(num,p=0, f=False):
    num = num+(num*(p/100))
    if f:
        return moeda(num)
    return num

def diminuir(num,p=0, f=False):
    num = num-(num*(p/100))
    if f:
        return moeda(num)
    return num

def moeda(num):
    return f'R${num},'