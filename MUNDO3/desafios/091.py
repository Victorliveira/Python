# Programa onde 4 jogadores tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado

from random import randint
from time import sleep

jogos = dict()

#Sorteador de dados
for c in range(1,5):
    jogos[f'Jogador {c}'] = randint(1,6)

#Apresenta os valores sorteados por cada jogador
print('Valores Sorteados')
sleep(1)
for k,v in jogos.items():
    print(f'O {k} tirou {v}')
    sleep(0.8)

#Apresenta o ranking dos jogadores usando como base os valores dos dados

jogosorted = dict(sorted(jogos.items(), key=lambda item: item[1], reverse=True))

print('\nRanking dos jogadores')
sleep(1)
cont = 1
for k,v in jogosorted.items():
    print(f'{cont}° lugar: {k} com {v}')
    cont +=1
    sleep(0.8)