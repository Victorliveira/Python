
def resumo(num,a,r):
    print('-'*40)
    print(f"{'RESUMO DO VALOR':^20}")
    print('-'*40)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{a}% de aumento: \t{aumentar(num,a, True)}')
    print(f'{r}% de redução: \t{diminuir(num,r, True)}')
    print('-'*40)

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

def moeda(num, formato='R$'):
    return f'{formato}{num:.2f}'.replace('.',',')