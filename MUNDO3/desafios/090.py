# Programa que leia o nome e média de um aluno, guardando també a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
# 7> Aprovado. Abaixo reprovado

dados = dict()

dados['Nome'] = str(input('Nome: ')).capitalize()
dados['Média'] = float(input(f'Média de {dados['Nome']}: '))
if dados['Média'] >= 7:
    dados['Situação'] = 'Aprovado'
elif 5 <= dados['Média'] < 7:
    dados['Situação'] = 'Recuperação'
else:
    dados['Situação'] = 'Reprovado'

print('-='*20)
for k,v in dados.items():
    print(f'{k} é igual a {v}') 