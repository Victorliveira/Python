#Programa que le vários num e coloca numa lista. a- quantos números foram digitados. b-a lista de valores descrescente. c-Se o valor 5 foi digitado e está ou n na lista

num = []
cont= 0

while True:
    numad = int(input('Digite um valor: '))
    num.append(numad)
    cont +=1
    parar = input('Deseja continuar? S/N ').upper()
    while parar not in ('SN'):
        print('Operação incorreta, digite novamente!')
        parar = input('Deseja continuar? S/N ').upper()
    if parar == 'N':
        break

print(f'Foram digitados {cont} valores.')
num.sort(reverse=True)
print(f'Lista em ordem descrescente: {num}')
if 5 in num:
    print(f'O valor 5 foi digitado e está nas posições ', end='')
    for pos, c in enumerate(num):
        if c == 5:
            print(f'{pos}..', end='')
else:
    print('O valor 5 não está na lista')