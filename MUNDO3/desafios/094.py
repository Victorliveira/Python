# Progama que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: a- Quantas pessoas foram cadastradas. b- A média de idade do grupo. c- Uma lista com todas as mulheres. d- Uma lista com todas as pessoas com idade acima da média.

dados = dict()
grupo = list()
soma = media = 0

while True:
    dados.clear()
    dados['Nome'] = str(input('Nome: ')).capitalize()
    dados['Idade'] = int(input('Idade: '))
    dados['Sexo'] = str(input('Sexo [M/F]: '))[0].upper()
    while dados['Sexo'] not in 'MF':
         print('Erro. Digite apenas M ou F!')
         dados['Sexo'] = str(input('Sexo [M/F]: '))[0].upper()
    soma += dados['Idade']
    grupo.append(dados.copy())
    seguir = str(input('Deseja continuar? [S/N] '))[0].upper()
    while seguir not in 'NS':
        print('Erro. Digite apenas N ou S!')
        seguir = str(input('Deseja continuar? [S/N] '))[0].upper()
    if seguir == 'N':
        break

media = soma/len(grupo)

print('-='*30)
print(f'- O grupo tem {len(grupo)} pessoas')
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram:', end= ' ')
# mostra o nome das mulheres cadastradas
for p,c in enumerate(grupo):
    if c['Sexo'] == 'F':
        print(c['Nome'], end=' ')

print(f'\n- Lista das pessoas que estão acima da média de idade: ')
print()
# mostra as pessoas acima da média de idade  
for p,c in enumerate(grupo):
    if c['Idade'] >= media:
        for k,v in c.items():
            print(f'    {k} = {v};', end=' ')
        print()

print('<<ENCERRADO>>')