#Programa que vai ler vários num e colocar em uma lista. Depois crie duas listas extras que vão conter apenas os valores pares e os ímpares. No final mostre o conteúdo das 3 listas geradas.

num = []

while True:
    numad = int(input('Digite um número: '))
    num.append(numad)
    parar = input('Deseja continuar? S/N ').upper()
    while parar not in ('SN'):
        print('Operação inválida, digite novamente!')
        parar = input('Deseja continuar? S/N ').upper()
    if parar == 'N':
        break


listapar = num[:]
listaimpar = num[:]

for v in num:
    if v %2 ==0:
        listaimpar.remove(v)
    else:
        listapar.remove(v)
listapar.sort()
listaimpar.sort()
print(f'Lista completa: {num}')
print(f'Lista com pares: {listapar}')
print(f'Lista com ímpares: {listaimpar}')