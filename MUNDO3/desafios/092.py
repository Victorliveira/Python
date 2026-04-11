# Programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário se por acaso o CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar

from datetime import datetime

dados = dict()

dados['nome'] = str(input('Nome: '))
ano = int(input('Ano de Nascimento: '))
anoatual = datetime.now().year
dados['idade'] = anoatual - ano

dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = (dados['contratação'] - ano) +35

print('-='*30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')