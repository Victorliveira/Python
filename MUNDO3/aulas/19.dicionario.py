# Variáveis Compostas - Dicionário 

# Dicionário é uma coleção de dados do tipo chave:valor, onde cada chave é única.

dic = {'nome':'Pedro','idade':25}
dic['sexo'] = 'M' # Adiciona a chave 'sexo' no dicionário
del dic['idade'] # Deleta a chave idade

filme= {'titulo':'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
}
print(filme.values()) # Retorna todos os valores do dicionário

print(filme.keys()) # Retorna todas as chaves

print(filme.items()) # Retorna os valores e chaves 

for k,v in filme.items():
    print(f'O {k} é {v}') 


brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])


estado = dict()
br = list()

for c in range(0,3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('sigla: '))
    br.append(estado.copy())

for e in br:
    print(e)