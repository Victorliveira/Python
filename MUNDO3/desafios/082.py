#Programa que vai ler vários num e colocar em uma lista. Depois crie duas listas extras que vão conter apenas os valores pares e os ímpares. No final mostre o conteúdo das 3 listas geradas.

num = []
listapar = []
listaimpar = []

while True:
    num.append(int(input('Digite um número: ')))
    parar = input('Deseja continuar? S/N ').upper()
    while parar not in ('SN'):
        print('Operação inválida, digite novamente!')
        parar = input('Deseja continuar? S/N ').upper()
    if parar == 'N':
        break

for v in num:
    if v %2 ==0:
        listapar.append(v)
    else:
        listaimpar.append(v)

print(f'Lista completa: {num}')
print(f'Lista com pares: {listapar}')
print(f'Lista com ímpares: {listaimpar}')