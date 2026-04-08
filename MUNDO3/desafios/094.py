# Progama que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: a- Quantas pessoas foram cadastradas. b- A média de idade do grupo. c- Uma lista com todas as mulheres. d- Uma lista com todas as pessoas com idade acima da média.

dados = dict()
grupo = list()
contp = mediai = 0

while True:
    dados['Nome'] = str(input('Nome: ')).capitalize()
    dados['Idade'] = int(input('Idade: '))
    dados['Sexo'] = str(input('Sexo [M/F]: '))[0].upper()
    while dados['Sexo'] not in 'MF':
         print('Operação Inválida. Digite novamente!')
         dados['Sexo'] = str(input('Sexo [M/F]: '))[0].upper()
    contp+=1
    mediai += dados['Idade']
    grupo.append(dados.copy())
    seguir = str(input('Deseja continuar? [S/N] '))[0].upper()
    while seguir not in 'NS':
        print('Operação Inválida. Digite novamente!')
        seguir = str(input('Deseja continuar? [S/N] '))[0].upper()
    if seguir == 'N':
        break

mediai = mediai/contp

print('-='*30)
print(f'- O grupo tem {contp} pessoas')
print(f'- A média de idade é de {mediai:.2f} anos.')
print(f'- As mulheres cadastradas foram:', end= ' ')
# mostra o nome das mulheres cadastradas
for p,c in enumerate(grupo):
    if grupo[p]['Sexo'] == 'F':
            for k,v in c.items():
                 if k == 'Nome':
                      print(v, end=' ')


print(f'\n- Lista das pessoas que estão acima da média de idade: ')

# mostra as pessoas acima da média de idade  
for p,c in enumerate(grupo):
    if grupo[p]['Idade'] >= mediai:
        print()
        for k,v in c.items():
            print(f'{k} = {v};', end=' ')
        print()

print('<<ENCERRADO>>')