
def resumo(num,a,r):
    print('-'*40)
    print(f"{'RESUMO DO VALOR':^40}")
    print('-'*40)
    print(f'Preço analisado: \t{moeda(num):>2}')
    print(f'Dobro do preço: \t{dobro(num, True):>2}')
    print(f'Metade do preço: \t{metade(num, True):>2}')
    print(f'{a}% de aumento: \t{aumentar(num,a, True):>2}')
    print(f'{r}% de redução: \t{diminuir(num,r, True):>2}')
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

def moeda(num):
    return f'R${num:.2f}'.replace('.',',')