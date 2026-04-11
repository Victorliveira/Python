# Programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a qtde de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato

campeonato = dict()
partida = dict()
gols = list()
total = 0

campeonato['nome'] = str(input('Nome do Jogador: ')).capitalize()
partidas = int(input(f'Quantas partidas {campeonato['nome']} jogou? '))

for c in range(partidas):
    partida[f'partida {c+1}'] = int(input(f'Quantos gols na partida {c+1}? '))
    total += partida[f'partida {c+1}']
    gols.append(partida[f'partida {c+1}'])


campeonato['gols'] = gols[:]
campeonato['total'] = total

print('-='*30)
for k,v in campeonato.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*30)
print(f'O jogador {campeonato["nome"]} jogou {len(campeonato["gols"])} partidas.')
for k,v in partida.items():
    print(f'    => Na {k}, fez {v} gols.')
print(f'Foi um total de {campeonato["total"]} gols')