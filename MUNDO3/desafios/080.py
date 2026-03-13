#Programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção. No final, mostre a lista ordenada na tela

num = []
for c in range(0,5):
    numad = int(input('Digite um valor: '))
    for pos, v in enumerate(num):
        if numad > num[-1]:
            num.append(numad)
            print('Valor adicionado na última posição')
            break
        if numad <= v:
            num.insert(pos, numad)
            print(f'Valor adicionado na posição {pos}')
            break
    if c == 0:
        num.append(numad)
        print(f'Valor adicionado na posição ', num.index(numad))
print('-='*35)
print(f'Os valores digitados em ordem foram {num}')
