#programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre, a-quantas pessoas foram cadastradas. b-uma listagem com as pessoas mais pesadas. c- Uma listagem com as pessoas mais leves
#b e c analisar o maior e menor peso cadastrados 

pessoas = list()
dados = list()

#Cadastrar uma quantidade sem limite de pessoas e seus pesos
while True:
    dados.append(str(input('Nome: ').capitalize()))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    parar = input('Deseja continuar? [S/N] ').upper()
    if parar not in ('SN'):
        print('Operação inválida! Digite novamente')
        parar = input('Deseja continuar? [S/N] ').upper()
    if parar == 'N':
        break

# Pega o maior e menor valor dentro da lista
maxpeso = max(pessoas, key=lambda pessoa: pessoa[1])[1]
minpeso = min(pessoas, key=lambda pessoa: pessoa[1])[1]

print('-='*40)


print(f'{len(pessoas)} pessoas foram cadastradas.')

print(f'O maior peso registrado foi {maxpeso}Kg.', end=' ')
for p, v in enumerate(pessoas):
    if pessoas[p][1] == maxpeso:
        print(pessoas[p][0], end=' ')
print(f'\nO menor peso registrado foi {minpeso}Kg.', end=' ')
for p, v in enumerate(pessoas):
    if pessoas[p][1] == minpeso:
        print(pessoas[p][0], end='.. ')