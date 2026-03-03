#Programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção. No final, mostre a lista ordenada na tela

num = []
for c in range(0,5):
    numad = int(input('Digite um valor: '))
    if c == 0:
        num.append(numad)
        print(num)
    for v in num:
        maxnum = max(num)
        minnum = min(num)
        if numad > maxnum:
            maxnumid = num.index(maxnum)
            num.insert(maxnumid +1, numad)
            print(f'Valor adicionado na posição {num.index(numad)}')
        elif numad < minnum:
            minnumid = num.index(minnum)
            num.insert(minnumid - 1, numad)
            print(f'Valor adicionado na posição {num.index(numad)}')
             
print('-='*35)
num.sort()
print(f'Os valores digitados em ordem foram {num}')
